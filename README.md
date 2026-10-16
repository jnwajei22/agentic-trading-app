# Agentic Trading Desk backend

FastAPI owns Auth0 verification, encrypted TradeLocker connections, market providers, risk-reviewed demo execution, autonomous profiles/schedules and the native AI assistant. The standalone `jnwajei22/agentic-trading-dashboard` repository is the only frontend. Inbound ChatGPT MCP, local OAuth authorization/token issuance, widget serving and the embedded bridge frontend are retired.

## Run

Use Python 3.11+, install `requirements.txt`, and configure `.env.example` on the backend host. Preserve the existing SQLite file and encryption keys; no PostgreSQL cutover occurs in this release. Start `uvicorn app.main:app`. Keep the existing persistent scheduler worker deployment and controls.

The assistant requires `OPENAI_API_KEY` and an explicit `AGENT_MODEL` only on FastAPI. Missing configuration fails closed. Auth0 still requires `AUTH_ISSUER`, `AUTH_AUDIENCE` and `AUTH_JWKS_URL`. The audience identifier can retain its existing value even if its name contains “mcp.” Keep BROKER_SECRET_KEY / BROKER_SECRET_KEYS_JSON / ACTIVE_ENCRYPTION_KEY_VERSION; all account-resolution paths now decrypt with the stored key version.

The model cannot enable autonomy, disable a kill switch, change risk limits, select another user's account or approve its own co-op actions. Autonomous operation uses the existing profile-bound **demo** engine. No live trading was added.

## Verification

From this repository: `RUN_TRADELOCKER_INTEGRATION=0 python -m pytest -q`. Tests use temporary SQLite and mocked broker/model clients. The explicitly opt-in real broker read test stays skipped. Do not run live broker tests as part of this change.

## Design and future persistence

See [native assistant architecture](docs/architecture/native-assistant.md) for API/streaming contracts, mode matrix, before/after diagrams, PostgreSQL ownership/deletion rules, and exact source-predicate migration scope. [postgresql-proposal.sql](docs/architecture/postgresql-proposal.sql) is design-only DDL: never run it at application startup. Neon remains untouched, SQLite remains authoritative, and there is no Alembic/import framework.
