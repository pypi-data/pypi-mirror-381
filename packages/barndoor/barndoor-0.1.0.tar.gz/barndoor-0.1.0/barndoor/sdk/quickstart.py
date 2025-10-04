"""Quick-start helpers that remove the boiler-plate required in the
examples/sample_agent.py script.

The three public async helpers cover the parts that tend to repeat in every
prototype:

    1. ``login_interactive`` – obtain a user JWT (cached) **and** a ready
       ``BarndoorSDK`` instance in one go.
    2. ``ensure_server_connected`` – wrapper around
       :pymeth:`barndoor.sdk.client.BarndoorSDK.ensure_server_connected` with a
       sensible progress / timeout default.
    3. ``get_mcp_adapter`` – construct a ``crewai_tools.MCPServerAdapter`` (or
       any other framework-agnostic adapter) that already carries the correct
       proxy URL, streaming transport and *provider* access token in the
       ``Authorization`` header.

The helpers are intentionally dependency-free – they import optional packages
only when necessary.  They can therefore be used both inside the Barndoor SDK
repo and by downstream projects that vendor-copy the file.
"""

from __future__ import annotations

# Standard library
import asyncio
import logging
from uuid import uuid4

# Import required auth helpers explicitly so type checkers can resolve them
from barndoor.sdk.auth import (
    build_authorization_url,
    exchange_code_for_token_backend,
    get_pending_oauth_state,
    start_local_callback_server,
)

# Automatically load .env if not done yet
from barndoor.sdk.config import get_static_config, load_dotenv_for_sdk

from .auth_store import (
    load_user_token,
    save_user_token,
)

# Load default .env file exactly once – safe no-op if already loaded by caller
load_dotenv_for_sdk()

# Internal imports -----------------------------------------------------------
from .client import BarndoorSDK
from .logging import get_logger

logger = get_logger("quickstart")


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------


a_sync = asyncio.run  # tiny alias for examples


async def login_interactive(
    *,
    auth_domain: str | None = None,
    client_id: str | None = None,
    client_secret: str | None = None,
    audience: str | None = None,
    api_base_url: str | None = None,
    port: int = 52765,
) -> BarndoorSDK:
    """Return an initialized BarndoorSDK after ensuring valid user JWT."""
    from .auth_store import is_token_active_with_refresh

    logger.info("Starting interactive login flow")

    cfg = get_static_config()

    auth_domain = auth_domain or cfg.auth_domain
    client_id = client_id or cfg.client_id
    client_secret = client_secret or cfg.client_secret
    audience = audience or cfg.api_audience  # Use config value

    # 1. try cached token with refresh first ----------------------------------
    token_data = None
    base_url = api_base_url or getattr(cfg, "api_base_url", None)
    if base_url and await is_token_active_with_refresh(base_url):
        logger.info("Using cached/refreshed valid token")
        token_data = load_user_token()
    else:
        # Only require client credentials if we need to perform OAuth
        if not client_id or not client_secret:
            raise RuntimeError(
                "AGENT_CLIENT_ID / AGENT_CLIENT_SECRET not set – "
                "create a .env file or export in the shell"
            )

        logger.info("No valid cached token, starting OAuth flow")
        # 2. if none – run interactive PKCE flow --------------------------
        redirect_uri, waiter = start_local_callback_server(port=port)
        auth_url = build_authorization_url(
            domain=auth_domain,
            client_id=client_id,
            redirect_uri=redirect_uri,
            audience=audience,
        )
        import webbrowser

        webbrowser.open(auth_url)
        logging.getLogger(__name__).info("Please complete login in your browser…")
        code, returned_state = await waiter
        # Validate OAuth state (if available) to mitigate CSRF
        expected_state = get_pending_oauth_state()
        if expected_state is not None and returned_state != expected_state:
            raise RuntimeError("OAuth state mismatch; possible CSRF attempt")
        token_data = exchange_code_for_token_backend(
            domain=auth_domain,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
        )
        save_user_token(token_data)

    # Extract access token for SDK
    access_token = token_data if isinstance(token_data, str) else token_data["access_token"]

    # 3. build dynamic configuration
    from barndoor.sdk.config import get_dynamic_config

    cfg_dyn = get_dynamic_config(access_token)
    api_base_url = api_base_url or cfg_dyn.api_base_url

    # 4. create SDK
    sdk = BarndoorSDK(api_base_url, barndoor_token=access_token, validate_token_on_init=False)
    logger.info("Login completed successfully")
    return sdk


async def ensure_server_connected(
    sdk: BarndoorSDK,
    server_identifier: str,
    *,
    timeout: int = 90,
) -> None:
    """Guarantee that *server_identifier* (slug or provider) is connected.

    If the server is already connected the coroutine is a no-op, otherwise it
    launches the browser OAuth flow and waits (up to *timeout* seconds) until
    the connection is live.
    """
    logger.info(f"Ensuring {server_identifier} server is connected")

    servers = await sdk.list_servers()
    server = next((s for s in servers if s.slug == server_identifier), None)

    if not server:
        logger.error(f"Server '{server_identifier}' not found")
        raise ValueError(f"Server '{server_identifier}' not found")

    if server.connection_status == "connected":
        logger.info(f"Server {server_identifier} already connected")
        return

    logger.info(f"Connecting to {server_identifier}...")
    await sdk.ensure_server_connected(server_identifier, poll_seconds=timeout)


async def make_mcp_connection_params(
    sdk: BarndoorSDK,
    server_slug: str,
    *,
    transport: str = "streamable-http",
):
    """Return ``(params_dict, public_url)`` where *params_dict* has the keys

    ``url``, ``headers`` and (optionally) ``transport`` so that it can be fed
    directly to whatever framework you’re using (CrewAI, LangChain, custom).

    The helper hides the rules:
      • If BARNDOOR_ENV is "prod" → build public MCP URL
        otherwise ("dev" or "local") → route through the local proxy.
      • Inject JWT + session-id headers
    """
    # 1. find the server and use proxy_url provided by registry
    servers = await sdk.list_servers()
    server = next((s for s in servers if s.slug == server_slug), None)
    if not server:
        raise ValueError(f"Server '{server_slug}' not found for current user")

    # Always prefer registry-provided proxy_url; fall back to detailed proxy_url
    url = getattr(server, "proxy_url", None)
    if not url:
        details = await sdk.get_server(server.id)
        url = getattr(details, "proxy_url", None)

    if not url:
        raise RuntimeError(
            "Registry did not provide a proxy_url for this server. Ensure backend is updated."
        )

    params = {
        "url": url,
        "transport": transport,
        "headers": {
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {sdk.token}",
            "x-barndoor-session-id": str(uuid4()),
        },
    }

    return params, url
