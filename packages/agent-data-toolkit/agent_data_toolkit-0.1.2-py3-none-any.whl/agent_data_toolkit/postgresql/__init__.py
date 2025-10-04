"""
Lazy re-exports for the PostgreSQL connector so importing the package
doesn't require optional dependencies until a symbol is actually used.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Final

__all__ = [
    "ConnectionInfo",
    "ConnectionManager",
    "PostgresClient",
    "query_rows",
    "query_df",
    "stream_to_parquet",
    "list_tables",
    "list_columns",
    "schema",
    "explain",
]

# Type checkers get precise symbols without importing heavy deps at runtime.
if TYPE_CHECKING:
    from .client import PostgresClient
    from .connection import ConnectionInfo, ConnectionManager
    from .queries import query_df, query_rows, stream_to_parquet
    from .schema import explain, list_columns, list_tables, schema  # noqa: F401

# Minimal lazy re-export map (module_path, attribute_name)
_ATTRS: Final[dict[str, tuple[str, str]]] = {
    "ConnectionInfo": ("agent_data_toolkit.postgresql.connection", "ConnectionInfo"),
    "ConnectionManager": ("agent_data_toolkit.postgresql.connection", "ConnectionManager"),
    "PostgresClient": ("agent_data_toolkit.postgresql.client", "PostgresClient"),
    "query_rows": ("agent_data_toolkit.postgresql.queries", "query_rows"),
    "query_df": ("agent_data_toolkit.postgresql.queries", "query_df"),
    "stream_to_parquet": ("agent_data_toolkit.postgresql.queries", "stream_to_parquet"),
    "list_tables": ("agent_data_toolkit.postgresql.schema", "list_tables"),
    "list_columns": ("agent_data_toolkit.postgresql.schema", "list_columns"),
    "schema": ("agent_data_toolkit.postgresql.schema", "schema"),
    "explain": ("agent_data_toolkit.postgresql.schema", "explain"),
}


def __getattr__(name: str):
    if name not in _ATTRS:
        raise AttributeError(name)
    mod_name, attr = _ATTRS[name]
    try:
        mod = importlib.import_module(mod_name)
        return getattr(mod, attr)
    except ImportError as e:
        # Optional deps likely missing (e.g., psycopg/pandas/pyarrow).
        raise RuntimeError(
            "PostgreSQL connector requires optional dependencies. "
            "Install them with: pip install 'agent-data-toolkit[postgresql]'"
        ) from e


def __dir__():
    return sorted(set(list(globals().keys()) + __all__))
