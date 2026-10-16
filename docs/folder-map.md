# Folder map

| Path | Responsibility |
|---|---|
| app/api/routes | Authenticated platform/assistant endpoints, legacy estimates and health |
| app/auth | Auth0 JWT verification and request identity |
| app/config | Runtime settings and versioned credential encryption |
| app/storage | Existing SQLite business repositories and two-table assistant history |
| app/services/agent | Native tool schemas, policy/ownership enforcement and OpenAI streaming |
| app/services/desk_tools.py | Transport-independent business wrappers extracted from inbound MCP |
| app/services/autonomous | Existing profile decision, control, risk-reviewed execution and reconciliation |
| app/services/market_data | Candle retrieval, pagination and bounded caches |
| app/services/providers | Finnhub/FRED clients |
| app/services/trading | Estimates and preview helpers |
| app/brokers | TradeLocker client, scoped mappings and explicit paper adapter |
| app/jobs | Persistent autonomous scheduler |
| app/webhooks | Untrusted TradingView signal ingress |
| tests | Unit, integration and release safety tests |
| docs/architecture | Current design, implementation report and unapplied PostgreSQL proposal |

The standalone dashboard is maintained in `jnwajei22/agentic-trading-dashboard`. No embedded frontend, MCP transport, widget build or local OAuth issuer is needed to start FastAPI.
