import errno
import socket
import time
import typing as t
import webbrowser
from datetime import UTC, datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib import parse
from urllib.error import HTTPError

import jwt
import requests
from pydantic import BaseModel, SecretStr
from requests_oauthlib import OAuth2Session

from aignostics.platform._messages import AUTHENTICATION_FAILED, INVALID_REDIRECT_URI
from aignostics.platform._settings import settings

CALLBACK_PORT_RETRY_COUNT = 10
try:
    import sentry_sdk
except ImportError:
    sentry_sdk = None  # type: ignore[assignment]


class AuthenticationResult(BaseModel):
    """Represents the result of an OAuth authentication flow."""

    token: str | None = None
    error: str | None = None


def _inform_sentry_about_user(token: str) -> None:
    """Inform Sentry about the authenticated user from the JWT token.

    Args:
        token: The JWT access token to extract user information from.

    Raises:
        RuntimeError: If the token does not contain the 'sub' claim or if verification fails.
    """
    if sentry_sdk is None:
        return  # type: ignore[unreachable]

    def _raise_missing_sub_claim_error() -> None:
        """Raises RuntimeError for missing 'sub' claim in token.

        Raises:
            RuntimeError: If the 'sub' claim is missing from the token.
        """
        message = "Token does not contain 'sub' claim, cannot set Sentry user info."
        raise RuntimeError(message)

    try:
        claims = verify_and_decode_token(token)
        user_id = claims.get("sub", None)
        if user_id is None:
            _raise_missing_sub_claim_error()
        sentry_sdk.set_user({"id": user_id, "org_id": claims.get("org_id", None)})
    except (jwt.InvalidTokenError, RuntimeError):
        # Don't fail authentication if Sentry user setup fails
        # Only catch specific exceptions related to token processing
        pass


def get_token(use_cache: bool = True, use_device_flow: bool = False) -> str:
    """Retrieves an authentication token, either from cache or via login.

    Args:
        use_cache (bool): Boolean indicating whether to store & use the token from disk cache.
            Defaults to True.
        use_device_flow (bool): Boolean indicating whether to force the usage of the device flow for authentication.

    Returns:
        str: The JWT access token.

    Raises:
        RuntimeError: If token retrieval fails.
    """
    token = None

    # Try to get token from cache first
    if use_cache and settings().token_file.exists():
        stored_token = Path(settings().token_file).read_text(encoding="utf-8")
        # Parse stored string "token:expiry_timestamp"
        parts = stored_token.split(":")
        cached_token, expiry_str = parts
        expiry = datetime.fromtimestamp(int(expiry_str), tz=UTC)

        # Check if token is still valid (with some buffer time)
        if datetime.now(tz=UTC) + timedelta(minutes=5) < expiry:
            token = cached_token

    # If no valid cached token, authenticate to get a new one
    if token is None:
        # If we end up here, we:
        # 1. Do not want to use the cached token
        # 2. The cached token is expired
        # 3. No token was cached yet
        token = _authenticate(use_device_flow)
        claims = verify_and_decode_token(token)

        # Store new token with expiry
        if use_cache:
            timestamp = claims["exp"]
            settings().token_file.parent.mkdir(parents=True, exist_ok=True)
            Path(settings().token_file).write_text(f"{token}:{timestamp}", encoding="utf-8")

    # Inform Sentry about the authenticated user (regardless of token source)
    _inform_sentry_about_user(token)

    return token


def remove_cached_token() -> bool:
    """Removes the cached authentication token.

    Deletes the token file if it exists, effectively logging out the user.

    Returns:
        bool: True if the token file was successfully removed, False if it did not exist.
    """
    if settings().token_file.exists():
        settings().token_file.unlink(missing_ok=True)
        return True
    return False


def _authenticate(use_device_flow: bool) -> str:
    """Allows the user to authenticate and obtain an access token.

    Determines the appropriate authentication flow based on whether
    a browser can be opened, then executes that flow.

    Args:
        use_device_flow (bool): Boolean indicating whether to force the usage of the device flow for authentication.

    Returns:
        str: The JWT access token.

    Raises:
        RuntimeError: If authentication fails.
        AssertionError: If the returned token doesn't have the expected format.
    """
    if refresh_token := settings().refresh_token:
        token = _token_from_refresh_token(refresh_token)
    elif _can_open_browser() and not use_device_flow:
        token = _perform_authorization_code_with_pkce_flow()
    else:
        token = _perform_device_flow()
    if not token:
        raise RuntimeError(AUTHENTICATION_FAILED)
    return token


def verify_and_decode_token(token: str) -> dict[str, str]:
    """
    Verifies and decodes the JWT token using the public key from JWS JSON URL.

    Args:
        token (str): The JWT token to verify and decode.

    Returns:
        dict[str,str]: The decoded token claims.

    Raises:
        RuntimeError: If token verification or decoding fails.
    """
    jwk_client = jwt.PyJWKClient(settings().jws_json_url)
    try:
        # Get the public key from the JWK client
        key = jwk_client.get_signing_key_from_jwt(token).key

        # Verify and decode the token using the public key
        # Reg. disabling verify_iat see https://github.com/jpadilla/pyjwt/issues/814,
        # and https://github.com/aignostics/python-sdk/actions/runs/15687051813/job/44192774617
        decoded = t.cast(
            "dict[str, str]",
            jwt.decode(
                token, key=key, algorithms=["RS256"], audience=settings().audience, options={"verify_iat": False}
            ),
        )
        # On verifying the issuer (iss),
        # see https://auth0.com/docs/manage-users/organizations/configure-organizations/use-org-name-authentication-api#recommended-best-practices
        if "iss" in decoded and decoded["iss"] != settings().issuer:
            message = f"Token issuer mismatch: expected {settings().issuer}, got {decoded['iss']}"
            raise RuntimeError(message)
        return decoded
    except jwt.exceptions.PyJWTError as e:
        raise RuntimeError(AUTHENTICATION_FAILED) from e


def _can_open_browser() -> bool:
    """Checks if a browser can be opened for authentication.

    Returns:
        bool: True if a browser can be opened, False otherwise.
    """
    launch_browser = False
    try:
        _ = webbrowser.get()
        launch_browser = True
    except webbrowser.Error:
        launch_browser = False

    return launch_browser


def _perform_authorization_code_with_pkce_flow() -> str:
    """Performs the OAuth 2.0 Authorization Code flow with PKCE.

    Opens a browser for user authentication and uses a local redirect
    to receive the authorization code.

    Returns:
        str: The JWT access token.

    Raises:
        RuntimeError: If authentication fails.
    """
    session = OAuth2Session(
        settings().client_id_interactive,
        scope=settings().scope_elements,
        redirect_uri=settings().redirect_uri,
        pkce="S256",
    )
    authorization_url, _ = session.authorization_url(
        settings().authorization_base_url,
        access_type="offline",
        audience=settings().audience,
    )

    authentication_result = AuthenticationResult()

    class OAuthCallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = parse.urlparse(self.path)
            query = parse.parse_qs(parsed.query)

            if "code" not in query:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Error: No authorization code received")
                authentication_result.error = "No authorization code received"
                return

            auth_code = query["code"][0]
            try:
                # Exchange code for token
                token = session.fetch_token(settings().token_url, code=auth_code, include_client_id=True)
                # Store the token
                authentication_result.token = token["access_token"]
                # Send success response
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"""
                    <html>
                        <script type="application/javascript">
                            setTimeout(function() { window.close(); }, 1000);
                        </script>
                        <body>
                            <h1>Authentication Successful!</h1>
                            <p>You can close this window now.</p>
                        </body>
                    </html>
                """)

            # we want to catch all exceptions here, so we can display them in the browser
            except Exception as e:  # noqa: BLE001
                # Display error message in browser
                self.send_response(500)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Error: {e!s}".encode())
                authentication_result.error = str(e)

        # Silence server logs
        def log_message(self, _format: str, *_args) -> None:  # type: ignore[no-untyped-def] # noqa: PLR6301
            return

    # Create and start the server
    parsed_redirect = parse.urlparse(settings().redirect_uri)
    host, port = parsed_redirect.hostname, parsed_redirect.port
    if not host or not port:
        raise RuntimeError(INVALID_REDIRECT_URI)
    # check if port is callback port is available
    port_unavailable_msg = f"Port {port} is already in use. Free the port, or use the device flow."
    if not _ensure_local_port_is_available(port):
        raise RuntimeError(port_unavailable_msg)
    # start the server
    try:
        with HTTPServer((host, port), OAuthCallbackHandler) as server:
            # Enable socket reuse to prevent "Address already in use" errors
            # This allows the socket to be reused immediately after the server closes,
            # even if the previous connection is in TIME_WAIT state
            server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Call Auth0 with challenge and redirect to localhost with code after successful authN
            webbrowser.open_new(authorization_url)
            # Extract authorization_code from redirected request, see: OAuthCallbackHandler
            server.handle_request()
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            raise RuntimeError(port_unavailable_msg) from e
        raise RuntimeError(AUTHENTICATION_FAILED) from e

    if authentication_result.error or not authentication_result.token:
        raise RuntimeError(AUTHENTICATION_FAILED)

    return authentication_result.token


def _perform_device_flow() -> str | None:
    """Performs the OAuth 2.0 Device Authorization flow.

    Used when a browser cannot be opened. Provides a URL for the user to visit
    on another device and polls for authorization completion.

    Returns:
        str | None: The JWT access token.

    Raises:
        ValueError: If no client id is configured for device flow.
        RuntimeError: If authentication fails or is denied.
    """
    client_id_device = settings().client_id_device
    if not client_id_device:
        message = (
            "No client id configured for device flow. Please set 'AIGNOSTICS_CLIENT_ID_DEVICE' in your environment."
        )
        raise ValueError(message)
    response = requests.post(
        settings().device_url,
        data={
            "client_id": client_id_device.get_secret_value(),
            "scope": settings().scope_elements,
            "audience": settings().audience,
        },
        timeout=settings().request_timeout_seconds,
    )
    try:
        response.raise_for_status()
        json_response = response.json()
        device_code = json_response["device_code"]
        verification_uri = json_response["verification_uri_complete"]
        user_code = json_response["user_code"]
        interval = int(json_response["interval"])
        print(
            f"Your user code is: {user_code}.\nPlease visit: {verification_uri} and verify the same code is displayed!"
        )

    except HTTPError as e:
        raise RuntimeError(AUTHENTICATION_FAILED) from e

    # Polling for access token with received device code
    while True:
        try:
            json_response = requests.post(
                settings().token_url,
                headers={"Accept": "application/json"},
                data={
                    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                    "device_code": device_code,
                    "client_id": client_id_device.get_secret_value(),
                },
                timeout=settings().request_timeout_seconds,
            ).json()
            if "error" in json_response:
                if json_response["error"] in {"authorization_pending", "slow_down"}:
                    time.sleep(interval)
                    continue
                raise RuntimeError(AUTHENTICATION_FAILED)

            return t.cast("str", json_response["access_token"])
        except requests.exceptions.JSONDecodeError as e:
            # Handle case where response is not JSON
            raise RuntimeError(AUTHENTICATION_FAILED) from e
        except HTTPError as e:
            raise RuntimeError(AUTHENTICATION_FAILED) from e


def _token_from_refresh_token(refresh_token: SecretStr) -> str | None:
    """Obtains a new access token using a refresh token.

    Args:
        refresh_token (SecretStr): The refresh token to use for obtaining a new access token.

    Returns:
        str | None: The new JWT access token.

    Raises:
        RuntimeError: If token refresh fails.
    """
    try:
        response = requests.post(
            settings().token_url,
            headers={"Accept": "application/json"},
            data={
                "grant_type": "refresh_token",
                "client_id": settings().client_id_interactive,
                "refresh_token": refresh_token.get_secret_value(),
            },
            timeout=settings().request_timeout_seconds,
        )
        response.raise_for_status()
        return t.cast("str", response.json()["access_token"])
    except (HTTPError, requests.exceptions.RequestException) as e:
        raise RuntimeError(AUTHENTICATION_FAILED) from e


def _ensure_local_port_is_available(port: int, max_retries: int = CALLBACK_PORT_RETRY_COUNT) -> bool:
    """Check if a port is already in use.

    Args:
        port (int): The port number to check.
        max_retries (int): The maximum number of retries to check the port.

    Returns:
        bool: True if the port is not in use, False otherwise.
    """

    def is_port_available() -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Enable socket reuse to match the behavior of the actual HTTPServer
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(("localhost", port))
                return True
            except OSError:
                return False

    retry_count = 0
    while not is_port_available() and retry_count < max_retries:
        time.sleep(1)
        retry_count += 1
    return retry_count < max_retries
