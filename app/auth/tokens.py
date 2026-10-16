import jwt
from jwt import PyJWKClient
from app.config.settings import settings

_jwks_clients: dict[str, PyJWKClient] = {}

def _verify_access_token(token: str) -> dict:
    if not settings.auth_issuer or not settings.auth_jwks_url or not settings.auth_audience:
        raise RuntimeError("OAuth issuer and JWKS URL must be configured.")
    client = _jwks_clients.setdefault(
        settings.auth_jwks_url, PyJWKClient(settings.auth_jwks_url)
    )
    signing_key = client.get_signing_key_from_jwt(token)
    return jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256", "RS384", "RS512", "ES256", "ES384", "ES512"],
        audience=settings.auth_audience,
        issuer=settings.auth_issuer,
        options={"require": ["exp", "iss", "aud"]},
    )
