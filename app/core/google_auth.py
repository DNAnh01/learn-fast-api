from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.starlette_client import OAuth
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app.core.config import settings

oauth = OAuth()

oauth.register(
    name="google",
    client_id=f"{settings.GOOGLE_CLIENT_ID}",
    client_secret=f"{settings.GOOGLE_CLIENT_SECRET}",
    client_kwargs={
        "scope": "email openid profile",
        "redirect_url": f"{settings.REDIRECT_URL}",
    },
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
)

async def authorize_access_token(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
        return token
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
