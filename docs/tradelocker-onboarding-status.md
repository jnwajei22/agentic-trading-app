# TradeLocker onboarding status contract

`transaction_valid` and `csrf_token` after validating the pending transaction.

Every connection-status response contains:

```json
{
  "status": "not_connected",
  "connected": false,
  "selected_account": null,
  "message": null,
  "retryable": false
}
```

The supported status values are:

| Status | Meaning | Onboarding action |
| --- | --- | --- |
| `not_connected` | No stored TradeLocker credentials | Connection form |
| `connected_no_account` | Credentials are valid but no returned account is selected | Account selection |
| `ready` | Credentials are valid and the selected account was rediscovered | Setup completion |
| `invalid_credentials` | TradeLocker rejected the saved credentials or server | Reconnect form |
| `expired` | The saved TradeLocker authentication is expired | Reconnect form |
| `unavailable` | TradeLocker or the status service cannot currently be checked | Centered retry state |

`selected_account` is non-null only for `ready` and contains only `account_id`,
`account_number`, and `server`. Missing, malformed, or unknown status values must
be treated as `unavailable`; they must never crash server rendering.

browser transaction reference is handled by the frontend before the status call.
failure returns HTTP 403.

## Pre-authorization authentication

creates a single-use, 60-second `Onboarding` assertion bound to the opaque
transaction reference. The backend verifies its HMAC signature, allowed issuer,
backend audience, Auth0 subject, transaction digest, expiry, and nonce. The
assertion is server-to-server and must never be returned to browser JavaScript.

Configure the same `ONBOARDING_ASSERTION_SECRET` on the backend and Vercel.
Vercel. The backend may allow both production and local issuers with:

```dotenv
ONBOARDING_ASSERTION_ISSUERS=https://agentic-forex-app.vercel.app,http://localhost:3000
```
