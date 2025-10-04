from __future__ import annotations

import types
from contextlib import contextmanager

import pytest


class FakeCursor:
    def __init__(self):
        self._sql = None
        # Minimal "description" to mimic psycopg so .fetchall() is valid
        self.description = [("ok",)]

    def execute(self, sql, params=None):
        self._sql = str(sql)
        # Ensure description is truthy after every execute
        self.description = [("ok",)]

    def fetchall(self):
        return [{"ok": 1}]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeConn:
    autocommit = True

    def cursor(self, name=None):
        return FakeCursor()

    @contextmanager
    def transaction(self):
        yield

    def close(self):
        pass


@pytest.fixture(autouse=True)
def _patch_conn(monkeypatch):
    """
    Patch connection creation + psycopg bits so tests don't need a real DB.
    """
    import agent_data_toolkit.postgresql.connection as conn_mod

    # Never open a real socket; always hand back our FakeConn
    monkeypatch.setattr(
        conn_mod.ConnectionManager,
        "_try_connect_once",
        lambda self, dsn: FakeConn(),
    )

    # Provide a minimal psycopg shim with the attributes we use
    def _fake_import_psycopg():
        sql_mod = types.SimpleNamespace(SQL=str, Identifier=str, Literal=lambda x: x)
        fake_psycopg = types.SimpleNamespace(sql=sql_mod)
        dict_row = object()  # not used by the fakes, but keeps signatures intact
        return fake_psycopg, dict_row

    monkeypatch.setattr(conn_mod, "_import_psycopg", _fake_import_psycopg)


@pytest.fixture
def client():
    from agent_data_toolkit.postgresql import PostgresClient
    return PostgresClient.from_dsn("postgresql://fake/fakedb")
