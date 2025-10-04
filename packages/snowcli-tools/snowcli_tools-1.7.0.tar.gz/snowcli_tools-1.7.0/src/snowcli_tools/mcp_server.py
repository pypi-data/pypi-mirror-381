"""FastMCP-powered MCP server that layers snowcli-tools features on top of
Snowflake's official MCP service implementation.

This module boots a FastMCP server, reusing the upstream Snowflake MCP runtime
(`snowflake-labs-mcp`) for authentication, connection management, middleware,
transport wiring, and its suite of Cortex/object/query tools. On top of that
foundation we register the snowcli-tools catalog, lineage, and dependency
workflows so agents can access both sets of capabilities via a single MCP
endpoint.
"""

from __future__ import annotations

import argparse
import os
from contextlib import asynccontextmanager
from functools import partial
from pathlib import Path
from typing import Any, Dict, Optional

import anyio
from pydantic import Field
from typing_extensions import Annotated

# NOTE: For typing, import from the fastmcp package; fallback handled at runtime.
try:  # Prefer the standalone fastmcp package when available
    from fastmcp import Context, FastMCP
    from fastmcp.utilities.logging import configure_logging, get_logger
except ImportError:  # Fall back to the implementation bundled with python-sdk
    from mcp.server.fastmcp import Context, FastMCP  # type: ignore[import-untyped,assignment]
    from mcp.server.fastmcp.utilities.logging import configure_logging, get_logger  # type: ignore[import-untyped,assignment]

from mcp_server_snowflake.server import (  # type: ignore[import-untyped]
    SnowflakeService,
)
from mcp_server_snowflake.server import (
    create_lifespan as create_snowflake_lifespan,  # type: ignore[import-untyped]
)
from mcp_server_snowflake.utils import (  # type: ignore[import-untyped]
    get_login_params,
    warn_deprecated_params,
)

from .config import Config, ConfigError, apply_config_overrides, get_config, load_config
from .context import create_service_context
from .lineage import LineageQueryService
from .lineage.identifiers import parse_table_name
from .mcp.utils import get_profile_recommendations, json_compatible
from .mcp_health import (
    MCPHealthMonitor,
)
from .mcp_resources import MCPResourceManager
from .profile_utils import (
    ProfileValidationError,
    get_profile_summary,
    validate_and_resolve_profile,
)
from .service_layer import CatalogService, DependencyService, QueryService
from .session_utils import (
    SessionContext,
    apply_session_context,
    ensure_session_lock,
    restore_session_context,
    snapshot_session,
)
from .snow_cli import SnowCLI, SnowCLIError
from .sql_validation import validate_sql_statement

_get_profile_recommendations = get_profile_recommendations

logger = get_logger(__name__)

# Global health monitor and resource manager instances
_health_monitor: Optional[MCPHealthMonitor] = None
_resource_manager: Optional[MCPResourceManager] = None
_catalog_service: Optional[CatalogService] = None


def _get_catalog_summary_sync(catalog_dir: str) -> Dict[str, Any]:
    service = _catalog_service
    if service is None:
        context = create_service_context(existing_config=get_config())
        service = CatalogService(context=context)
    return service.load_summary(catalog_dir)


def _execute_query_sync(
    snowflake_service: Any,
    statement: str,
    overrides: Dict[str, Optional[str]] | SessionContext,
) -> Dict[str, Any]:
    lock = ensure_session_lock(snowflake_service)
    with lock:
        with snowflake_service.get_connection(  # type: ignore[attr-defined]
            use_dict_cursor=True,
            session_parameters=snowflake_service.get_query_tag_param(),  # type: ignore[attr-defined]
        ) as (_, cursor):
            original = snapshot_session(cursor)
            try:
                if overrides:
                    apply_session_context(cursor, overrides)
                cursor.execute(statement)
                rows = cursor.fetchall()
                return {
                    "statement": statement,
                    "rowcount": cursor.rowcount,
                    "rows": rows,
                }
            finally:
                restore_session_context(cursor, original)


def _query_lineage_sync(
    object_name: str,
    direction: str,
    depth: int,
    fmt: str,
    catalog_dir: str,
    cache_dir: str,
    config: Config,
) -> Dict[str, Any]:
    """Query lineage graph for a specific object.

    Raises:
        ValueError: If object is not found in lineage graph
    """
    service = LineageQueryService(
        catalog_dir=Path(catalog_dir), cache_root=Path(cache_dir)
    )

    default_db = config.snowflake.database
    default_schema = config.snowflake.schema
    qualified = parse_table_name(object_name).with_defaults(default_db, default_schema)
    base_key = qualified.key()
    candidates = [base_key]
    if not base_key.endswith("::task"):
        candidates.append(f"{base_key}::task")

    result = None
    resolved_key: Optional[str] = None
    for candidate in candidates:
        try:
            result = service.object_subgraph(
                candidate, direction=direction, depth=depth
            )
        except KeyError:
            continue
        resolved_key = candidate
        break

    if result is None or resolved_key is None:
        raise ValueError(
            f"Object '{object_name}' not found in lineage graph. "
            f"Run build_catalog first or verify the object name. "
            f"Catalog directory: {catalog_dir}"
        )

    payload: Dict[str, Any] = {
        "object": resolved_key,
        "direction": direction,
        "depth": depth,
        "node_count": len(result.graph.nodes),
        "edge_count": len(result.graph.edge_metadata),
    }

    if fmt == "json":
        payload["graph"] = (
            result.graph.to_dict()
            if hasattr(result.graph, "to_dict")
            else json_compatible(result.graph)
        )
    else:
        summary = [
            f"- {node.attributes.get('name', key)} ({node.node_type.value})"
            for key, node in result.graph.nodes.items()
        ]
        payload["summary"] = "\n".join(summary)

    return payload


def register_snowcli_tools(
    server: FastMCP,
    snowflake_service: SnowflakeService,
    *,
    enable_cli_bridge: bool = False,
) -> None:
    """Register snowcli-tools MCP endpoints on top of the official service."""

    if getattr(server, "_snowcli_tools_registered", False):  # pragma: no cover - safety
        return
    setattr(server, "_snowcli_tools_registered", True)

    config = get_config()
    context = create_service_context(existing_config=config)
    query_service = QueryService(context=context)
    catalog_service = CatalogService(context=context)
    dependency_service = DependencyService(context=context)
    global _health_monitor, _resource_manager, _catalog_service
    _health_monitor = context.health_monitor
    _resource_manager = context.resource_manager
    _catalog_service = catalog_service
    snow_cli: SnowCLI | None = SnowCLI() if enable_cli_bridge else None

    @server.tool(
        name="execute_query", description="Execute a SQL query against Snowflake"
    )
    async def execute_query_tool(
        statement: Annotated[str, Field(description="SQL statement to execute")],
        warehouse: Annotated[
            Optional[str], Field(description="Warehouse override", default=None)
        ] = None,
        database: Annotated[
            Optional[str], Field(description="Database override", default=None)
        ] = None,
        schema: Annotated[
            Optional[str], Field(description="Schema override", default=None)
        ] = None,
        role: Annotated[
            Optional[str], Field(description="Role override", default=None)
        ] = None,
        timeout_seconds: Annotated[
            Optional[int],
            Field(
                description="Query timeout in seconds (default: 120s from config)",
                ge=1,
                le=3600,
                default=None,
            ),
        ] = None,
        verbose_errors: Annotated[
            bool,
            Field(
                description="Include detailed optimization hints in error messages (default: false for compact errors)",
                default=False,
            ),
        ] = False,
        ctx: Context | None = None,
    ) -> Dict[str, Any]:
        """Execute a SQL query against Snowflake with optional timeout and error verbosity control.

        Args:
            statement: SQL statement to execute
            warehouse: Optional warehouse override
            database: Optional database override
            schema: Optional schema override
            role: Optional role override
            timeout_seconds: Query timeout in seconds (default: 120s). Use higher values for complex queries.
            verbose_errors: Include detailed error messages with optimization hints (default: false for compact errors)

        Returns:
            Query results with rows, rowcount, and execution metadata

        Raises:
            ValueError: If profile validation fails, SQL is blocked, or query execution encounters validation errors
            RuntimeError: If query execution fails due to connection, timeout, or other runtime issues
        """
        # Validate profile health before executing query
        if _health_monitor:
            profile_health = await anyio.to_thread.run_sync(
                _health_monitor.get_profile_health,
                config.snowflake.profile,
                False,  # use cache
            )
            if not profile_health.is_valid:
                error_msg = (
                    profile_health.validation_error or "Profile validation failed"
                )
                available = (
                    ", ".join(profile_health.available_profiles)
                    if profile_health.available_profiles
                    else "none"
                )
                _health_monitor.record_error(f"Profile validation failed: {error_msg}")
                raise ValueError(
                    f"Snowflake profile validation failed: {error_msg}. "
                    f"Profile: {config.snowflake.profile}, "
                    f"Available profiles: {available}. "
                    f"Check configuration with 'snow connection list' or verify profile settings."
                )

        # Validate SQL statement against permissions
        allow_list = config.sql_permissions.get_allow_list()
        disallow_list = config.sql_permissions.get_disallow_list()

        stmt_type, is_valid, error_msg = validate_sql_statement(
            statement, allow_list, disallow_list
        )

        if not is_valid and error_msg:
            if _health_monitor:
                _health_monitor.record_error(
                    f"SQL statement blocked: {stmt_type} - {statement[:100]}"
                )
            raise ValueError(error_msg)

        overrides = {
            "warehouse": warehouse,
            "database": database,
            "schema": schema,
            "role": role,
        }
        packed = {k: v for k, v in overrides.items() if v}

        # Determine timeout (use provided value or config default)
        timeout = (
            timeout_seconds if timeout_seconds is not None else config.timeout_seconds
        )

        try:
            session_ctx = query_service.session_from_mapping(packed)

            # Execute with timeout using asyncio.wait_for
            result = await anyio.fail_after(
                timeout,
                anyio.to_thread.run_sync,
                partial(
                    query_service.execute_with_service,
                    snowflake_service,
                    statement,
                    session=session_ctx,
                ),
            )

            if ctx is not None:
                await ctx.debug(
                    f"Executed query with {len(result['rows'])} rows (rowcount={result['rowcount']})."
                )

            return result

        except anyio.get_cancelled_exc_class() as e:
            # Handle timeout
            if _health_monitor:
                _health_monitor.record_error(
                    f"Query timeout after {timeout}s: {statement[:100]}"
                )

            if verbose_errors:
                # Verbose mode: detailed optimization hints (~200-300 tokens)
                raise RuntimeError(
                    f"Query timeout after {timeout}s.\n\n"
                    f"Quick fixes:\n"
                    f"1. Increase timeout: execute_query(..., timeout_seconds={timeout * 4})\n"
                    f"2. Add filter: Add WHERE clause to reduce data volume\n"
                    f"3. Sample data: Add LIMIT clause for testing (e.g., LIMIT 1000)\n"
                    f"4. Scale warehouse: Consider using a larger warehouse for complex queries\n\n"
                    f"Current settings:\n"
                    f"  - Timeout: {timeout}s\n"
                    f"  - Warehouse: {warehouse or config.snowflake.warehouse or 'default'}\n"
                    f"  - Database: {database or config.snowflake.database or 'default'}\n\n"
                    f"Query preview: {statement[:150]}{'...' if len(statement) > 150 else ''}\n\n"
                    f"Use verbose_errors=False for compact error messages."
                ) from e
            else:
                # Compact mode: concise guidance (~80-100 tokens)
                raise RuntimeError(
                    f"Query timeout ({timeout}s). "
                    f"Try: timeout_seconds={timeout * 4}, add WHERE/LIMIT clause, or scale warehouse. "
                    f"Use verbose_errors=True for detailed optimization hints."
                ) from e

        except ProfileValidationError as e:
            if _health_monitor:
                _health_monitor.record_error(
                    f"Query execution failed - profile error: {e}"
                )
            raise ValueError(f"Profile validation failed: {e}") from e
        except Exception as e:
            if _health_monitor:
                _health_monitor.record_error(f"Query execution failed: {e}")

            if verbose_errors:
                # Verbose mode: include more context
                raise RuntimeError(
                    f"Query execution failed: {e}\n\n"
                    f"Context:\n"
                    f"  - Statement: {statement[:200]}{'...' if len(statement) > 200 else ''}\n"
                    f"  - Warehouse: {warehouse or config.snowflake.warehouse or 'default'}\n"
                    f"  - Database: {database or config.snowflake.database or 'default'}\n"
                    f"  - Schema: {schema or config.snowflake.schema or 'default'}\n\n"
                    f"Use verbose_errors=False for compact error messages."
                ) from e
            else:
                # Compact mode: brief error
                raise RuntimeError(
                    f"Query execution failed: {e}. "
                    f"Statement: {statement[:100]}{'...' if len(statement) > 100 else ''}. "
                    f"Use verbose_errors=True for details."
                ) from e

    @server.tool(name="preview_table", description="Preview table contents")
    async def preview_table_tool(
        table_name: Annotated[str, Field(description="Fully qualified table name")],
        limit: Annotated[int, Field(description="Row limit", ge=1, default=100)] = 100,
        warehouse: Annotated[
            Optional[str], Field(description="Warehouse override", default=None)
        ] = None,
        database: Annotated[
            Optional[str], Field(description="Database override", default=None)
        ] = None,
        schema: Annotated[
            Optional[str], Field(description="Schema override", default=None)
        ] = None,
        role: Annotated[
            Optional[str], Field(description="Role override", default=None)
        ] = None,
    ) -> Dict[str, Any]:
        statement = f"SELECT * FROM {table_name} LIMIT {limit}"
        overrides = {
            "warehouse": warehouse,
            "database": database,
            "schema": schema,
            "role": role,
        }
        packed = {k: v for k, v in overrides.items() if v}
        session_ctx = query_service.session_from_mapping(packed)
        return await anyio.to_thread.run_sync(
            partial(
                query_service.execute_with_service,
                snowflake_service,
                statement,
                session=session_ctx,
            )
        )

    @server.tool(name="build_catalog", description="Build Snowflake catalog metadata")
    async def build_catalog_tool(
        output_dir: Annotated[
            str,
            Field(description="Catalog output directory", default="./data_catalogue"),
        ] = "./data_catalogue",
        database: Annotated[
            Optional[str],
            Field(description="Specific database to introspect", default=None),
        ] = None,
        account: Annotated[
            bool, Field(description="Include entire account", default=False)
        ] = False,
        format: Annotated[
            str, Field(description="Output format (json/jsonl)", default="json")
        ] = "json",
        include_ddl: Annotated[
            bool, Field(description="Include object DDL", default=True)
        ] = True,
    ) -> Dict[str, Any]:
        def run_catalog() -> Dict[str, Any]:
            totals = catalog_service.build(
                output_dir,
                database=database,
                account_scope=account,
                incremental=False,
                output_format=format,
                include_ddl=include_ddl,
                max_ddl_concurrency=8,
                catalog_concurrency=16,
                export_sql=False,
            )
            return {
                "output_dir": output_dir,
                "totals": totals,
            }

        try:
            return await anyio.to_thread.run_sync(run_catalog)
        except Exception as exc:
            raise RuntimeError(f"Catalog build failed: {exc}") from exc

    @server.tool(name="query_lineage", description="Query cached lineage graph")
    async def query_lineage_tool(
        object_name: Annotated[str, Field(description="Object name to analyze")],
        direction: Annotated[
            str,
            Field(
                description="Traversal direction (upstream/downstream/both)",
                default="both",
            ),
        ] = "both",
        depth: Annotated[
            int, Field(description="Traversal depth", ge=1, le=10, default=3)
        ] = 3,
        format: Annotated[
            str, Field(description="Output format (text/json)", default="text")
        ] = "text",
        catalog_dir: Annotated[
            str,
            Field(description="Catalog directory", default="./data_catalogue"),
        ] = "./data_catalogue",
        cache_dir: Annotated[
            str,
            Field(description="Lineage cache directory", default="./lineage"),
        ] = "./lineage",
    ) -> Dict[str, Any]:
        result = await anyio.to_thread.run_sync(
            _query_lineage_sync,
            object_name,
            direction,
            depth,
            format,
            catalog_dir,
            cache_dir,
            config,
        )
        return result

    @server.tool(
        name="build_dependency_graph", description="Build object dependency graph"
    )
    async def build_dependency_graph_tool(
        database: Annotated[
            Optional[str], Field(description="Specific database", default=None)
        ] = None,
        schema: Annotated[
            Optional[str], Field(description="Specific schema", default=None)
        ] = None,
        account: Annotated[
            bool, Field(description="Include account-level metadata", default=False)
        ] = False,
        format: Annotated[
            str, Field(description="Output format (json/dot)", default="json")
        ] = "json",
    ) -> Dict[str, Any]:
        def run_graph() -> Dict[str, Any]:
            graph = dependency_service.build(
                database=database,
                schema=schema,
                account_scope=account,
            )
            if format == "dot":
                return {"format": "dot", "graph": dependency_service.to_dot(graph)}
            return {"format": "json", "graph": graph}

        return await anyio.to_thread.run_sync(run_graph)

    @server.tool(name="test_connection", description="Validate Snowflake connectivity")
    async def test_connection_tool() -> Dict[str, Any]:
        """Test Snowflake connection.

        Raises:
            RuntimeError: If connection test fails
        """
        ok = await anyio.to_thread.run_sync(
            partial(query_service.test_connection, snowflake_service)
        )
        if not ok:
            raise RuntimeError(
                "Snowflake connection test failed. "
                "Verify credentials, network connectivity, and warehouse availability."
            )
        return {"status": "connected", "message": "Connection test successful"}

    @server.tool(name="health_check", description="Get comprehensive health status")
    async def health_check_tool() -> Dict[str, Any]:
        """Get health status including connection state and system info."""
        try:
            version = getattr(__import__("snowcli_tools"), "__version__", "unknown")

            if _health_monitor:
                # Use the enhanced health monitor
                health = await anyio.to_thread.run_sync(
                    _health_monitor.get_comprehensive_health,
                    config.snowflake.profile,
                    snowflake_service,
                    [
                        "catalog",
                        "lineage",
                        "cortex",
                        "query_manager",
                        "semantic_manager",
                    ],  # Available resources
                    version,
                )
                return health.to_mcp_response()
            else:
                # Fallback to basic health check
                from .services import RobustSnowflakeService

                connection_ok = await anyio.to_thread.run_sync(
                    partial(query_service.test_connection, snowflake_service)
                )

                robust_service = RobustSnowflakeService(config.snowflake.profile)
                health_status = await anyio.to_thread.run_sync(
                    robust_service.get_health_status
                )

                return {
                    "status": (
                        "healthy"
                        if connection_ok and health_status.healthy
                        else "unhealthy"
                    ),
                    "snowflake_connection": connection_ok,
                    "detailed_health": {
                        "healthy": health_status.healthy,
                        "snowflake_connection": health_status.snowflake_connection,
                        "last_error": health_status.last_error,
                        "circuit_breaker_state": health_status.circuit_breaker_state,
                    },
                    "version": version,
                    "timestamp": anyio.current_time(),
                }
        except Exception as e:
            if _health_monitor:
                _health_monitor.record_error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": anyio.current_time(),
            }

    @server.tool(name="get_catalog_summary", description="Read catalog summary JSON")
    async def get_catalog_summary_tool(
        catalog_dir: Annotated[
            str,
            Field(description="Catalog directory", default="./data_catalogue"),
        ] = "./data_catalogue",
    ) -> Dict[str, Any]:
        return await anyio.to_thread.run_sync(
            partial(catalog_service.load_summary, catalog_dir)
        )

    @server.tool(
        name="check_profile_config", description="Check Snowflake profile configuration"
    )
    async def check_profile_config_tool() -> Dict[str, Any]:
        """Check current Snowflake profile configuration and provide diagnostics.

        Raises:
            RuntimeError: If profile configuration check fails
        """

        def _check_profile_sync() -> Dict[str, Any]:
            summary = get_profile_summary()
            current_profile = os.environ.get("SNOWFLAKE_PROFILE")

            # Try to validate current configuration
            validation_result: dict[str, Any] = {"valid": False, "error": None}
            try:
                resolved_profile = validate_and_resolve_profile()
                validation_result = {
                    "valid": True,
                    "resolved_profile": resolved_profile,
                    "error": None,
                }
            except ProfileValidationError as e:
                validation_result = {"valid": False, "error": str(e)}

            return {
                "config_path": str(summary.config_path),
                "config_exists": summary.config_exists,
                "available_profiles": summary.available_profiles,
                "profile_count": summary.profile_count,
                "default_profile": summary.default_profile,
                "current_profile": current_profile,
                "validation": validation_result,
                "recommendations": get_profile_recommendations(
                    summary, current_profile
                ),
            }

        try:
            return await anyio.to_thread.run_sync(_check_profile_sync)
        except Exception as e:
            raise RuntimeError(f"Failed to check profile configuration: {e}") from e

    @server.tool(
        name="get_resource_status",
        description="Get availability status for MCP server resources",
    )
    async def get_resource_status_tool(
        check_catalog: Annotated[
            bool, Field(description="Include catalog availability check", default=True)
        ] = True,
        catalog_dir: Annotated[
            str,
            Field(description="Catalog directory to check", default="./data_catalogue"),
        ] = "./data_catalogue",
    ) -> Dict[str, Any]:
        """Get comprehensive resource availability status.

        Raises:
            RuntimeError: If resource manager is unavailable or status check fails
        """
        if not _resource_manager:
            raise RuntimeError(
                "Resource manager not available. "
                "Server may not be fully initialized."
            )

        # Define core resources to check
        resource_names = [
            "catalog",
            "lineage",
            "cortex_search",
            "cortex_analyst",
            "query_manager",
            "object_manager",
            "semantic_manager",
        ]

        try:
            # Check resource availability
            resource_status = await anyio.to_thread.run_sync(
                partial(
                    _resource_manager.create_resource_status_response,
                    resource_names,
                    snowflake_service,
                    catalog_dir=catalog_dir if check_catalog else None,
                )
            )
            return resource_status

        except Exception as e:
            if _health_monitor:
                _health_monitor.record_error(f"Resource status check failed: {e}")
            raise RuntimeError(f"Failed to get resource status: {e}") from e

    @server.tool(
        name="check_resource_dependencies",
        description="Check dependencies for a specific resource",
    )
    async def check_resource_dependencies_tool(
        resource_name: Annotated[str, Field(description="Resource name to check")],
        catalog_dir: Annotated[
            str, Field(description="Catalog directory", default="./data_catalogue")
        ] = "./data_catalogue",
    ) -> Dict[str, Any]:
        """Check dependencies for a specific resource.

        Raises:
            RuntimeError: If resource manager is unavailable or dependency check fails
        """
        if not _resource_manager:
            raise RuntimeError(
                "Resource manager not available. "
                "Server may not be fully initialized."
            )

        try:
            # Get resource availability
            availability = await anyio.to_thread.run_sync(
                partial(
                    _resource_manager.get_resource_availability,
                    resource_name,
                    snowflake_service,
                    catalog_dir=catalog_dir,
                )
            )

            # Get recommendations
            recommendations = _resource_manager.get_resource_recommendations(
                resource_name, availability
            )

            # Get dependency information
            dependencies = _resource_manager.dependencies.get(resource_name, [])

            return {
                "resource_name": resource_name,
                "availability": availability.to_dict(),
                "dependencies": dependencies,
                "recommendations": recommendations,
                "timestamp": anyio.current_time(),
            }

        except Exception as e:
            if _health_monitor:
                _health_monitor.record_error(f"Resource dependency check failed: {e}")
            raise RuntimeError(f"Failed to check resource dependencies: {e}") from e

    if enable_cli_bridge and snow_cli is not None:

        @server.tool(
            name="run_cli_query",
            description="Execute a query via the Snowflake CLI bridge",
        )
        async def run_cli_query_tool(
            statement: Annotated[
                str, Field(description="SQL query to execute using snow CLI")
            ],
            warehouse: Annotated[
                Optional[str], Field(description="Warehouse override", default=None)
            ] = None,
            database: Annotated[
                Optional[str], Field(description="Database override", default=None)
            ] = None,
            schema: Annotated[
                Optional[str], Field(description="Schema override", default=None)
            ] = None,
            role: Annotated[
                Optional[str], Field(description="Role override", default=None)
            ] = None,
        ) -> Dict[str, Any]:
            overrides: Dict[str, Optional[str]] = {
                "warehouse": warehouse,
                "database": database,
                "schema": schema,
                "role": role,
            }
            ctx_overrides: Dict[str, Optional[str]] = {
                k: v for k, v in overrides.items() if v is not None
            }
            try:
                result = await anyio.to_thread.run_sync(
                    partial(
                        snow_cli.run_query,
                        statement,
                        output_format="json",
                        ctx_overrides=ctx_overrides,
                    )
                )
            except SnowCLIError as exc:
                raise RuntimeError(f"Snow CLI query failed: {exc}") from exc

            rows = result.rows or []
            return {
                "statement": statement,
                "rows": rows,
                "stdout": result.raw_stdout,
                "stderr": result.raw_stderr,
            }


def _apply_config_overrides(args: argparse.Namespace) -> Config:
    overrides = {
        key: value
        for key in ("profile", "warehouse", "database", "schema", "role")
        if (value := getattr(args, key, None))
    }

    try:
        cfg = load_config(
            config_path=args.snowcli_config,
            cli_overrides=overrides or None,
        )
    except ConfigError as exc:
        raise SystemExit(f"Failed to load configuration: {exc}") from exc

    if cfg.snowflake.profile:
        os.environ.setdefault("SNOWFLAKE_PROFILE", cfg.snowflake.profile)
        os.environ["SNOWFLAKE_PROFILE"] = cfg.snowflake.profile

    return cfg


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Snowflake MCP server with snowcli-tools extensions",
    )

    login_params = get_login_params()
    for value in login_params.values():
        if len(value) < 2:
            # Malformed entry; ignore to avoid argparse blow-ups
            continue

        help_text = value[-1]
        if len(value) >= 3:
            flags = value[:-2]
            default_value = value[-2]
        else:
            flags = value[:-1]
            default_value = None

        # Guard against implementations that only provide flags + help text
        if default_value == help_text:
            default_value = None

        parser.add_argument(
            *flags,
            required=False,
            default=default_value,
            help=help_text,
        )

    parser.add_argument(
        "--service-config-file",
        required=False,
        help="Path to Snowflake MCP service configuration YAML",
    )
    parser.add_argument(
        "--transport",
        required=False,
        choices=["stdio", "http", "sse", "streamable-http"],
        default=os.environ.get("SNOWCLI_MCP_TRANSPORT", "stdio"),
        help="Transport to use for FastMCP (default: stdio)",
    )
    parser.add_argument(
        "--endpoint",
        required=False,
        default=os.environ.get("SNOWCLI_MCP_ENDPOINT", "/mcp"),
        help="Endpoint path when running HTTP-based transports",
    )
    parser.add_argument(
        "--mount-path",
        required=False,
        default=None,
        help="Optional mount path override for SSE transport",
    )
    parser.add_argument(
        "--snowcli-config",
        required=False,
        help="Optional path to snowcli-tools YAML config (defaults to env)",
    )
    parser.add_argument(
        "--profile",
        required=False,
        help="Override Snowflake CLI profile for snowcli-tools operations",
    )
    parser.add_argument(
        "--enable-cli-bridge",
        action="store_true",
        help="Expose the legacy Snowflake CLI bridge tool (disabled by default)",
    )
    parser.add_argument(
        "--log-level",
        required=False,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default=os.environ.get("SNOWCLI_MCP_LOG_LEVEL", "INFO"),
        help="Log level for FastMCP runtime",
    )
    parser.add_argument(
        "--name",
        required=False,
        default="snowcli-tools MCP Server",
        help="Display name for the FastMCP server",
    )
    parser.add_argument(
        "--instructions",
        required=False,
        default="Snowcli-tools MCP server combining Snowflake official tools with catalog/lineage helpers.",
        help="Instructions string surfaced to MCP clients",
    )

    args = parser.parse_args(argv)

    # Mirror CLI behaviour for env overrides
    if not getattr(args, "service_config_file", None):
        args.service_config_file = os.environ.get("SERVICE_CONFIG_FILE")

    return args


def create_combined_lifespan(args: argparse.Namespace):
    snowflake_lifespan = create_snowflake_lifespan(args)

    @asynccontextmanager
    async def lifespan(server: FastMCP):
        global _health_monitor, _resource_manager

        # Initialize health monitor at server startup
        _health_monitor = MCPHealthMonitor(server_start_time=anyio.current_time())

        # Initialize resource manager with health monitor
        _resource_manager = MCPResourceManager(health_monitor=_health_monitor)

        # Perform early profile validation
        try:
            config = get_config()
            if config.snowflake.profile:
                profile_health = await anyio.to_thread.run_sync(
                    _health_monitor.get_profile_health,
                    config.snowflake.profile,
                    True,  # force_refresh
                )
                if not profile_health.is_valid:
                    logger.warning(
                        f"Profile validation issue detected: {profile_health.validation_error}"
                    )
                    _health_monitor.record_error(
                        f"Profile validation failed: {profile_health.validation_error}"
                    )
                else:
                    logger.info(
                        f"✓ Profile health check passed for: {profile_health.profile_name}"
                    )
        except Exception as e:
            logger.warning(f"Early profile validation failed: {e}")
            _health_monitor.record_error(f"Early profile validation failed: {e}")

        async with snowflake_lifespan(server) as snowflake_service:
            # Test Snowflake connection during startup
            try:
                connection_health = await anyio.to_thread.run_sync(
                    _health_monitor.check_connection_health, snowflake_service
                )
                if connection_health.value == "healthy":
                    logger.info("✓ Snowflake connection health check passed")
                else:
                    logger.warning(
                        f"Snowflake connection health check failed: {connection_health}"
                    )
            except Exception as e:
                logger.warning(f"Connection health check failed: {e}")
                _health_monitor.record_error(f"Connection health check failed: {e}")

            register_snowcli_tools(
                server,
                snowflake_service,
                enable_cli_bridge=args.enable_cli_bridge,
            )
            yield snowflake_service

    return lifespan


def main(argv: list[str] | None = None) -> None:
    """Main entry point for MCP server.

    Args:
        argv: Optional command line arguments. If None, uses sys.argv[1:].
               When called from CLI, should pass empty list to avoid argument conflicts.
    """
    args = parse_arguments(argv)

    warn_deprecated_params()
    configure_logging(level=args.log_level)
    _apply_config_overrides(args)

    # Validate Snowflake profile configuration before starting server
    try:
        # Use the enhanced validation function
        resolved_profile = validate_and_resolve_profile()

        logger.info(f"✓ Snowflake profile validation successful: {resolved_profile}")

        # Set the validated profile in environment for snowflake-labs-mcp
        os.environ["SNOWFLAKE_PROFILE"] = resolved_profile
        os.environ["SNOWFLAKE_DEFAULT_CONNECTION_NAME"] = resolved_profile

        # Update config with validated profile
        apply_config_overrides(snowflake={"profile": resolved_profile})

        # Log profile summary for debugging
        summary = get_profile_summary()
        logger.debug(f"Profile summary: {summary}")

    except ProfileValidationError as e:
        logger.error("❌ Snowflake profile validation failed")
        logger.error(f"Error: {e}")

        # Provide helpful next steps
        if e.available_profiles:
            logger.error(f"Available profiles: {', '.join(e.available_profiles)}")
            logger.error("To fix this issue:")
            logger.error(
                "1. Set SNOWFLAKE_PROFILE environment variable to one of the available profiles"
            )
            logger.error("2. Or pass --profile <profile_name> when starting the server")
            logger.error("3. Or run 'snow connection add' to create a new profile")
        else:
            logger.error("No Snowflake profiles found.")
            logger.error("Please run 'snow connection add' to create a profile first.")

        if e.config_path:
            logger.error(f"Expected config file at: {e.config_path}")

        # Exit with clear error code
        raise SystemExit(1) from e
    except Exception as e:
        logger.error(f"❌ Unexpected error during profile validation: {e}")
        raise SystemExit(1) from e

    server = FastMCP(
        args.name,
        instructions=args.instructions,
        lifespan=create_combined_lifespan(args),
    )

    try:
        logger.info("Starting FastMCP server using transport=%s", args.transport)
        if args.transport in {"http", "sse", "streamable-http"}:
            endpoint = os.environ.get("SNOWFLAKE_MCP_ENDPOINT", args.endpoint)
            server.run(
                transport=args.transport,
                host="0.0.0.0",
                port=9000,
                path=endpoint,
            )
        else:
            server.run(transport=args.transport)
    except Exception as exc:  # pragma: no cover - run loop issues bubble up
        logger.error("MCP server terminated with error: %s", exc)
        raise


if __name__ == "__main__":
    main()
