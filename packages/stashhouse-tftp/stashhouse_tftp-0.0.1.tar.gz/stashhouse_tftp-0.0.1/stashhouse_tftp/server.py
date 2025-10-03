# Copyright (c) 2025 Jayson Fong
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
TFTP plugin implementation for StashHouse.

Provides a Trivial File Transfer Protocol (TFTP) server for StashHouse
processing requests asynchronously and only permitting write operations.
"""

import asyncio
import logging
import multiprocessing
from typing import TYPE_CHECKING

import stashhouse_tftp.protocols


if TYPE_CHECKING:
    import stashhouse.server

logger = logging.getLogger(__name__)


# pylint: disable=too-few-public-methods
class TFTPServer:
    """
    Plugin to accept files over TFTP.

    Attributes:
        server_options: Server options applied globally.
        exited: Whether shutdown should be performed.
        port: Port to listen on.
        ack_timeout: Timeout for each ACK of the lock-step.
        conn_timeout: Timeout before aborting a connection.
    """

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(
        self,
        server_options: "stashhouse.server.ServerOptions",
        exited: multiprocessing.Event,
        port: int = 69,
        ack_timeout: float = 0.5,
        conn_timeout: float = 3.0,
    ):
        """
        Initialize the TFTP server.

        Args:
            server_options: Server options applied globally.
            exited: Whether shutdown should be performed.
            port: Port to listen on.
            ack_timeout: Timeout for each ACK of the lock-step.
            conn_timeout: Timeout before aborting a connection.
        """

        self.server_options: "stashhouse.server.ServerOptions" = server_options
        self.exited: multiprocessing.Event = exited
        self.port: int = port
        self.ack_timeout: float = ack_timeout
        self.conn_timeout: float = conn_timeout

    def _timeouts(self) -> dict[bytes, float]:
        return {b"ack_timeout": self.ack_timeout, b"conn_timeout": self.conn_timeout}

    async def _run(self):
        loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        try:
            # fmt: off
            transport, protocol = await loop.create_datagram_endpoint(
                lambda: stashhouse_tftp.protocols.TFTPServerProtocol(
                    self.server_options.host,
                    loop,
                    self._timeouts(),
                    data_directory=self.server_options.directory,
                ),
                local_addr=(
                    self.server_options.host, self.port,
                ),
            )

            del protocol
        except PermissionError:
            # fmt: off
            logger.exception(
                "A permission error occurred. Please verify that you have "
                "sufficient privileges to bind to the requested host: %s:%d",
                self.server_options.host, self.port
            )
            return

        while not self.exited.is_set():
            await asyncio.sleep(1.0)

        transport.close()
        loop.close()

    def run(self) -> None:
        """
        Executes the TFTP server using asyncio.
        """

        asyncio.run(self._run())


__all__ = ("TFTPServer",)
