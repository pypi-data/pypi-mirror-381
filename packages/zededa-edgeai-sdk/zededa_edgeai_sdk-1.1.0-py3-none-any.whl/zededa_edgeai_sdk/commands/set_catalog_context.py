"""Set catalog context command providing catalog switching with shell launch functionality.

Implements simplified catalog switching that combines catalog selection with
shell launching to provide an authenticated environment similar to login.
"""

from __future__ import annotations

import argparse
import os
from typing import Dict, Optional

from ..config import get_service_url
from ..environment import APPLIED_ENVIRONMENT_KEYS
from ..exceptions import AuthenticationError
from . import CommandSpec
from .catalogs import execute_catalog_switch


def handle_set_catalog_context(args: argparse.Namespace) -> None:  # pragma: no cover
    """Handle the set-catalog-context command when invoked from the CLI.
    
    Processes command-line arguments, executes catalog switching workflow,
    and sets authentication credentials in the current environment variables.
    """
    catalog_name = args.catalog
    service_url = getattr(args, "service_url", None) or get_service_url()
    debug = getattr(args, "debug", False)
    
    try:
        # Execute catalog switch to get credentials
        credentials = execute_catalog_switch(
            catalog_name,
            service_url=service_url,
            debug=debug,
        )
        
        current_catalog = credentials.get("catalog_id")
        print(f"Successfully switched to catalog: {current_catalog}")
        print("Environment variables have been set in the current shell.")
        print("The following credentials are now available:")
        for key in APPLIED_ENVIRONMENT_KEYS:
            value = os.environ.get(key)
            if value:
                if any(sensitive in key.upper() for sensitive in ["TOKEN", "KEY", "SECRET"]):
                    print(f"  {key}=***")
                else:
                    print(f"  {key}={value}")
        
    except KeyboardInterrupt:
        print("\nCatalog context switch cancelled by user.")
        raise SystemExit(1)
    except AuthenticationError as exc:
        print(f"Catalog context switch failed: {exc}")
        raise SystemExit(1) from exc
    except ValueError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc
    except Exception as exc:  # pragma: no cover - defensive
        print(f"Unexpected error during catalog context switch: {exc}")
        if debug:
            import traceback
            traceback.print_exc()
        raise SystemExit(1) from exc


def _register(subparsers: argparse._SubParsersAction) -> None:
    """Configure argparse with set-catalog-context command options and arguments.
    
    Defines the set-catalog-context subcommand with catalog name as a positional
    argument and optional service URL and debug settings.
    """
    parser = subparsers.add_parser(
        "set-catalog-context",
        help="Switch to catalog and set environment variables",
        description="Switch to the specified catalog and set "
                   "credentials in environment variables.",
    )
    parser.add_argument(
        "catalog",
        help="Catalog name to switch to"
    )
    parser.add_argument(
        "--service-url",
        help="EdgeAI service URL override (default: use EDGEAI_SERVICE_URL "
             "environment variable or https://studio.edgeai.zededa.dev)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    parser.set_defaults(_command_handler=handle_set_catalog_context)


SET_CATALOG_CONTEXT_COMMAND = CommandSpec(
    name="set-catalog-context",
    help="Switch to catalog and set environment variables",
    register=_register,
)