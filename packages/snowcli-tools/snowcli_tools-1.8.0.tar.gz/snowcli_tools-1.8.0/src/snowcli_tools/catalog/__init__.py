"""Unified catalog module for Snowflake data cataloging.

This module consolidates catalog functionality that was previously spread across:
- catalog.py (core implementation, 818 LOC)
- catalog_service.py (service layer classes, 273 LOC)
- service_layer/catalog.py (wrapper service, 85 LOC)

Total: 1,176 LOC consolidated into 450 LOC service.py
Reduction: ~726 LOC (62%)

Part of v1.8.0 refactoring Phase 1.1
"""

from __future__ import annotations

from .models import CatalogBuildResult, CatalogBuildTotals, CatalogMetadata
from .service import CatalogService, build_catalog, export_sql_from_catalog

__all__ = [
    "CatalogService",
    "build_catalog",
    "export_sql_from_catalog",
    "CatalogBuildResult",
    "CatalogBuildTotals",
    "CatalogMetadata",
]
