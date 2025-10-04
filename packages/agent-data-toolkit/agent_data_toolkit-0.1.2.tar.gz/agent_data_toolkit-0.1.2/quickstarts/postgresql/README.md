# Quickstart: PostgreSQL

Spin up a local PostgreSQL instance and try **agent-data-toolkit** from a Jupyter notebook.

This quickstart is self-contained: Docker brings up Postgres (seeded with a tiny schema and sample data), and a notebook shows how to connect, query, inspect schema, and export results.

## 1) Start PostgreSQL

1) Copy the environment file and adjust if desired:

```bash
cp .env.example .env
```

2) Bring up the database:

```bash
docker compose up -d
```

The service is named `mcp-postgres`, listens on `127.0.0.1:5432`, and is auto-seeded by the SQL files in `docker-entrypoint-initdb.d/` on first start.

## 2) Python environment

### Using uv (recommended)

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

```bash
Using pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3) Run the Notebooks

### 01_getting_started

* Open `notebooks/01_getting_started.ipynb` and run cells top-to-bottom.
* It will:
    * Read PG_DSN from your environment (set via .env)
    * Create a PostgresClient
    * Run a smoke test (SELECT 1)
    * Query the demo table into a DataFrame