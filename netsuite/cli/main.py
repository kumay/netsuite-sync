import argparse
import asyncio
import inspect
import logging
import sys

from ..constants import DEFAULT_INI_PATH, DEFAULT_INI_SECTION
from . import helpers, interact, misc, rest_api, restlet, soap_api

__all__ = ("main",)


def main():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-l",
        "--log-level",
        help="The log level to use",
        default="INFO",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
    )
    parser.add_argument(
        "-p",
        "--config-path",
        help="The config file to get settings from",
        default=DEFAULT_INI_PATH,
    )
    parser.add_argument(
        "-c",
        "--config-section",
        help="The config section to get settings from",
        default=DEFAULT_INI_SECTION,
    )

    subparser = parser.add_subparsers(help="App CLI", required=True)

    misc.add_parser(parser, subparser)
    interact.add_parser(parser, subparser)
    restlet_parser, _ = restlet.add_parser(parser, subparser)
    rest_api_parser, _ = rest_api.add_parser(parser, subparser)
    soap_api_parser, _ = soap_api.add_parser(parser, subparser)

    try:
        args = parser.parse_args()
    except Exception:
        parser.print_help()
        return

    subparser_name = sys.argv[-1]

    # Show help section instead of an error when no arguments were passed...
    if subparser_name == "rest-api":
        rest_api_parser.print_help()
        return
    elif subparser_name == "soap-api":
        rest_api_parser.print_help()
        return
    elif subparser_name == "restlet":
        restlet_parser.print_help()
        return

    config = helpers.load_config_or_error(parser, args.config_path, args.config_section)

    log_level = getattr(logging, args.log_level)
    logging.basicConfig(level=log_level)

    ret = args.func(config, args)

    if inspect.iscoroutinefunction(args.func):
        ret = asyncio.run(ret)

    if ret is not None:
        print(ret)
