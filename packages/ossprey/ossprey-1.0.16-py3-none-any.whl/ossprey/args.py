from __future__ import annotations
import argparse
import os
from argparse import Namespace
from typing import Optional

from ossprey.modes import get_all_modes


# Used to pull booleans from env vars
def get_bool(value: Optional[str]) -> bool:
    return value.lower() in ("true", "1", "yes", "on") if value else False


###
# Parse the command line arguments
# Please Note: Everything argument needs a default value otherwise tests will fail
# @return: The parsed arguments
###
def parse_arguments() -> Namespace:

    parser = argparse.ArgumentParser(description="API URL:")
    parser.add_argument(
        "--url",
        type=str,
        help="The URL to process",
        default=os.getenv("INPUT_URL", "https://api.ossprey.com")
    )
    parser.add_argument(
        "--package", "--dir",
        dest="package",
        type=str,
        help="The package or directory to scan",
        default=os.getenv("INPUT_PACKAGE", os.getcwd())
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run mode",
        default=get_bool(os.getenv("INPUT_DRY_RUN"))
    )
    parser.add_argument(
        "--github-comments",
        action="store_true",
        help="GitHub mode, will attempt to post comments to GitHub",
        default=get_bool(os.getenv("INPUT_GITHUB_COMMENTS"))
    )

    parser.add_argument(
        "--verbose", '-v',
        action="store_true",
        help="Verbose mode",
        default=get_bool(os.getenv("INPUT_VERBOSE"))
    )

    # Scanning methods
    parser.add_argument(
        '--mode',
        choices=get_all_modes(),
        help="Mode to generate the SBOM. Choose 'pipenv' to install the package or 'requirements' to provide a requirements file.",
        default=os.getenv("INPUT_MODE", 'auto')
    )

    # Authentication
    parser.add_argument(
        '--api-key',
        type=str,
        help="API Key to authenticate with the API.",
        default=os.getenv("API_KEY", None)
    )

    # Authentication
    parser.add_argument(
        '--soft-error',
        action="store_true",
        help="If the scan causes an error don't stop the CICD process from continuing",
        default=get_bool(os.getenv("INPUT_SOFT_ERROR"))
    )

    # Output
    parser.add_argument(
        '-o', '--output',
        type=str,
        help="Output file for the SBOM",
        default=os.getenv("INPUT_OUTPUT", None)
    )

    args = parser.parse_args()

    # Check if the API key is provided
    if args.api_key is None and args.dry_run is False:
        parser.error("--api_key or the environment variable API_KEY is required")

    return args
