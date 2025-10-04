from __future__ import annotations

from .connection import ConnectionInfo, ConnectionManager
from .queries import query_df, query_rows, stream_to_parquet
from .schema import explain as explain_plan
from .schema import list_columns, list_tables
from .schema import schema as schema_info


class PostgresClient:
    """Light façade around ConnectionManager with ergonomic helpers."""
    def __init__(self, manager: ConnectionManager):
        self._m = manager

    @classmethod
    def from_env(cls, **kwargs) -> PostgresClient:
        return cls(ConnectionManager.from_env(**kwargs))

    @classmethod
    def from_dsn(cls, dsn: str, **kwargs) -> PostgresClient:
        return cls(ConnectionManager(ConnectionInfo(dsn=dsn), **kwargs))

    @classmethod
    def from_info(cls, info: ConnectionInfo, **kwargs) -> PostgresClient:
        return cls(ConnectionManager(info, **kwargs))

    def __enter__(self) -> PostgresClient: return self
    def __exit__(self, exc_type, exc, tb) -> None: self.close()

    # Queries
    def query_rows(self, *args, **kwargs):
        return query_rows(self._m, *args, **kwargs)

    def query_df(self, *args, **kwargs):
        return query_df(self._m, *args, **kwargs)

    def stream_to_parquet(self, *args, **kwargs):
        return stream_to_parquet(self._m, *args, **kwargs)

    # Schema
    def list_tables(self, schema_name: str | None = None):
        return list_tables(self._m, schema_name)

    def list_columns(self, schema_name: str, table: str):
        return list_columns(self._m, schema_name, table)

    def schema(self, **kwargs):
        return schema_info(self._m, **kwargs)

    def explain(self, sql: str, **kwargs):
        return explain_plan(self._m, sql, **kwargs)

    # Lifecycle
    def close(self) -> None: self._m.close()
    def pool_health(self) -> dict: return self._m.pool_health()
