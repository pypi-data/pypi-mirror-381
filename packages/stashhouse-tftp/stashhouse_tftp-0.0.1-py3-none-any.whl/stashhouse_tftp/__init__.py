# Copyright (c) 2025 Jayson Fong
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Collection of files through TFTP.

Provides the option to collect files using the TFTP protocol.
"""

import argparse
from typing import Any

__version__ = "0.0.1"


def register_arguments(plugin_name: str, parser: argparse.ArgumentParser) -> None:
    """
    Registers arguments to an argument parser.

    Registers a port argument to an argument parser.

    Args:
        plugin_name: Name of the plugin to register arguments for.
        parser: Argument parser to register arguments into.
    """
    # fmt: off
    group = parser.add_argument_group(
        "Trivial File Transfer Protocol (TFTP)",
        description="Trivial File Transfer Protocol (TFTP) server options",
    )

    # fmt: off
    group.add_argument(
        f"--{plugin_name}.port",
        type=int, default=9069, dest=f"{plugin_name}.port",
        help="Port to listen on. (default: 9069)"
    )

    # fmt: off
    group.add_argument(
        f"--{plugin_name}.ack-timeout",
        type=float, default=0.5, dest=f"{plugin_name}.ack_timeout",
        help="Timeout for each ACK. (default: 0.5)"
    )

    # fmt: off
    group.add_argument(
        f"--{plugin_name}.conn-timeout",
        type=float, default=3.0, dest=f"{plugin_name}.conn_timeout",
        help='Timeout before aborting a connection. (default: 3.0)'
    )


def parse_arguments(plugin_name: str, args: argparse.Namespace) -> dict[str, Any]:
    """

    Args:
        plugin_name: Name of the plugin to register arguments for.
        args: Namespace to extract arguments from.

    Returns:
        A dictionary of arguments parsed from the command line.
        The dictionary keys are strings, and the dictionary
        itself is used for keyword arguments passed to initialize
        the plugin.
    """

    return {
        "port": getattr(args, f"{plugin_name}.port", 9069),
        "ack_timeout": getattr(args, f"{plugin_name}.ack_timeout", 0.5),
        "conn_timeout": getattr(args, f"{plugin_name}.conn_timeout", 3),
    }


__all__ = ("__version__", "register_arguments", "parse_arguments")
