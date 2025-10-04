"""Tests for package imports."""

import pytest


def test_import_main_package():
    """Test importing the main package."""
    import goodgleif  # noqa: F401


def test_import_companymatcher():
    """Test importing the main CompanyMatcher class."""
    from goodgleif.companymatcher import CompanyMatcher  # noqa: F401


def test_import_canonicalname():
    """Test importing canonical name functions."""
    from goodgleif.canonicalname import create_canonical_name, create_brief_name  # noqa: F401


def test_import_paths():
    """Test importing path utilities."""
    from goodgleif.paths import get_writable_dir, default_parquet_path  # noqa: F401


def test_import_whereami():
    """Test importing whereami utilities."""
    from goodgleif.whereami import get_project_root  # noqa: F401


def test_import_loader():
    """Test importing loader utilities."""
    from goodgleif.loader import build_small_csv  # noqa: F401


def test_import_query():
    """Test importing query utilities."""
    from goodgleif.companymatcher import CompanyMatcher  # noqa: F401


