"""Authentication command providing login functionality.

Implements both browser-based and credential-based authentication
workflows with environment setup for MLflow and storage access.
"""

from __future__ import annotations

import argparse
import os
from getpass import getpass
from typing import Any, Dict, Optional

import requests

from ..config import get_service_url
from ..zededa_edgeai_sdk import ZededaEdgeAISDK
from ..environment import (
    APPLIED_ENVIRONMENT_KEYS,
    apply_environment,
    sanitize_credentials,
)
from ..exceptions import AuthenticationError
from . import CommandSpec


def execute_login(
    catalog_id: Optional[str] = None,
    *,
    email: Optional[str] = None,
    password: Optional[str] = None,
    prompt_password: bool = False,
    service_url: Optional[str] = None,
    prompt_on_multiple: bool = True,
    debug: bool = False,
    sdk: ZededaEdgeAISDK | None = None,
) -> Dict[str, Any]:
    """Execute the complete login workflow and configure environment variables.
    
    Performs authentication using either browser OAuth or email/password credentials,
    handles catalog selection, retrieves storage credentials, and applies them to
    the current environment. Returns sanitized credentials for display.
    """

    if sdk is not None:
        service_url = sdk.edgeai_backend_url
    else:
        service_url = (service_url or get_service_url()).rstrip("/")
        sdk = ZededaEdgeAISDK(service_url, ui_url=service_url, debug=debug)

    assert sdk is not None  # Satisfy type-checkers
    normalized_catalog = _normalize_catalog(catalog_id)

    if email and not password and prompt_password:
        password = getpass("Password: ")

    if email and not password:
        raise ValueError(
            "Password is required when email is provided. "
            "Use prompt_password=True to be prompted for password."
        )
    if password and not email:
        raise ValueError("Email is required when password is provided")

    if email:
        raw_credentials = _login_with_credentials(
            sdk,
            service_url,
            normalized_catalog,
            email,
            password or "",
            prompt_on_multiple=prompt_on_multiple,
        )
    else:
        raw_credentials = _login_with_browser(
            sdk,
            normalized_catalog,
            prompt_on_multiple=prompt_on_multiple,
        )

    catalog_id = raw_credentials.get("catalog_id")
    env_vars = apply_environment(raw_credentials, catalog_id)
    raw_credentials["environment"] = env_vars
    return sanitize_credentials(raw_credentials)


def handle_cli(args: argparse.Namespace) -> None:  # pragma: no cover
    """Handle the login command when invoked from the CLI.
    
    Processes command-line arguments, executes the login workflow, and
    sets authentication credentials in the current environment variables.
    """
    service_url = getattr(args, "service_url", None) or get_service_url()
    debug = getattr(args, "debug", False)

    try:
        credentials = execute_login(
            args.catalog,
            email=getattr(args, "email", None),
            password=getattr(args, "password", None),
            prompt_password=getattr(args, "prompt_password", False),
            service_url=service_url,
            prompt_on_multiple=True,
            debug=debug,
        )
        print("Login successful. Environment variables have been set in the current shell.")
        print("The following credentials are now available:")
        for key in APPLIED_ENVIRONMENT_KEYS:
            value = os.environ.get(key)
            if value:
                if any(sensitive in key.upper() for sensitive in ["TOKEN", "KEY", "SECRET"]):
                    print(f"  {key}={_mask(value)}")
                else:
                    print(f"  {key}={value}")
    except KeyboardInterrupt:
        print("\nLogin cancelled by user.")
        raise SystemExit(1)
    except AuthenticationError as exc:
        print(f"Login failed: {exc}")
        raise SystemExit(1) from exc
    except ValueError as exc:
        print(exc)
        raise SystemExit(1) from exc
    except Exception as exc:  # pragma: no cover - defensive
        print(f"Unexpected error: {exc}")
        if debug:
            import traceback

            traceback.print_exc()
        raise SystemExit(1) from exc


def _normalize_catalog(catalog_id: Optional[str]) -> Optional[str]:
    """Clean and validate catalog ID input.
    
    Strips whitespace from catalog ID strings and returns None for
    empty or None values, ensuring consistent catalog ID handling.
    """
    if isinstance(catalog_id, str) and catalog_id.strip():
        return catalog_id.strip()
    return None


def _login_with_credentials(
    sdk: ZededaEdgeAISDK,
    service_url: str,
    catalog_id: Optional[str],
    email: str,
    password: str,
    *,
    prompt_on_multiple: bool,
) -> Dict[str, Any]:
    """Authenticate using email and password credentials.
    
    Sends login request to the backend API, handles catalog selection if needed,
    retrieves MinIO credentials, and returns complete authentication data
    including permissions and tokens.
    """
    url = f"{service_url}/api/v1/auth/login"
    payload = {"email": email, "password": password}
    if catalog_id:
        payload["catalog_id"] = catalog_id

    try:
        response = sdk._send_request(  # pylint: disable=protected-access
            "POST", url, json=payload
        )
    except requests.RequestException as exc:  # pragma: no cover
        raise AuthenticationError(f"Login request failed: {exc}") from exc

    if response.status_code != 200:
        raise AuthenticationError(
            f"Login failed with status {response.status_code}: "
            f"{response.text}"
        )

    try:
        data = response.json()
    except ValueError as exc:
        raise AuthenticationError("Login response is not valid JSON") from exc

    token = data.get("access_token")
    if not token:
        raise AuthenticationError("Login response missing access_token")

    selected_catalog, scoped_token = (
        sdk._resolve_catalog_selection(  # pylint: disable=protected-access
            token,
            catalog_id,
            prompt_on_multiple=prompt_on_multiple,
        )
    )

    if not selected_catalog or not scoped_token:
        raise AuthenticationError("Catalog selection failed or was cancelled")

    minio_credentials = sdk._get_minio_credentials(  # pylint: disable=protected-access
        scoped_token, selected_catalog
    )
    if not minio_credentials:
        raise AuthenticationError("Failed to fetch MinIO credentials")

    minio_credentials["catalog_id"] = selected_catalog
    minio_credentials["backend_jwt"] = scoped_token
    minio_credentials["token_type"] = data.get("token_type", "bearer")
    minio_credentials["expires_in"] = data.get("expires_in")
    minio_credentials["service_url"] = sdk.edgeai_backend_url
    return minio_credentials


def _login_with_browser(
    sdk: ZededaEdgeAISDK,
    catalog_id: Optional[str],
    *,
    prompt_on_multiple: bool,
) -> Dict[str, Any]:
    """Authenticate using browser-based OAuth flow.
    
    Opens a browser for user authentication, handles the OAuth callback,
    manages catalog selection when multiple catalogs are available, and
    returns complete credentials including storage access tokens.
    """
    credentials = sdk.login_with_browser(
        catalog_id, prompt_on_multiple=prompt_on_multiple
    )
    if not credentials:
        raise AuthenticationError("Browser login failed")
    credentials["service_url"] = sdk.edgeai_backend_url
    return credentials


def _mask(value: Optional[str], show: int = 4) -> Optional[str]:
    """Mask sensitive string values for safe console output.
    
    Obscures the middle portion of sensitive strings while preserving
    the beginning and end characters for identification purposes.
    Returns the original value if it's None or shorter than the show parameter.
    """
    if not value:
        return value
    if len(value) <= show:
        return value
    return f"{value[:show]}...{value[-2:]}"


def _register(subparsers: argparse._SubParsersAction) -> None:
    """Configure argparse with login command options and arguments.
    
    Defines all command-line options for the login command including
    catalog selection, authentication methods, service URL configuration,
    and debug settings.
    """
    parser = subparsers.add_parser(
        "login",
        help="Authenticate and configure environment",
        description="Authenticate with Zededa EdgeAI and set "
                   "credentials in environment variables.",
    )
    parser.add_argument("--catalog",
                       help="Catalog ID to authenticate against")
    parser.add_argument("--email",
                       help="Email for programmatic login (no browser)")
    parser.add_argument("--password",
                       help="Password for programmatic login (no browser)")
    parser.add_argument(
        "--prompt-password",
        action="store_true",
        help="Prompt for password if --email is provided and "
             "--password is omitted",
    )
    parser.add_argument(
        "--service-url",
        help="EdgeAI service URL (default: "
             "https://studio.edgeai.zededa.dev)"
    )
    parser.add_argument("--debug", action="store_true",
                       help="Enable debug logging")
    parser.set_defaults(_command_handler=handle_cli)


LOGIN_COMMAND = CommandSpec(
    name="login",
    help="Authenticate and configure environment",
    register=_register,
)
