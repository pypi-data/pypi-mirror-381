# Copyright (c) 2025 Jayson Fong
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Protocol implementations for TFTP.

Restricts operations to write-only.
"""

import logging
import pathlib
from typing import Callable

import py3tftp.tftp_packet
import py3tftp.protocols

import stashhouse_tftp.file_io

logger = logging.getLogger(__name__)


class OperationProhibitedProtocol(py3tftp.protocols.BaseTFTPProtocol):
    """
    TFTP protocol handler that does nothing.

    Sends an error on initialization to prevent activity.
    """

    __slots__: tuple[str, ...] = tuple()

    def handle_initialization(self) -> None:
        """
        Sends the first packet to the remote address, which
        will always indicate an access violation error.
        """
        self.set_proto_attributes()
        pkt = self.packet_factory.err_access_violation()
        self.send_opening_packet(pkt.to_bytes())
        self.handle_err_pkt()

    def next_datagram(self) -> None:
        """
        Would normally return the next datagram, but here is prohibited.

        Raises:
            PermissionError: The operation is prohibited.
        """
        raise PermissionError("Operation prohibited.")

    def datagram_received(self, data, addr) -> None:
        """
        Would normally process an incoming packet, but here is prohibited.

        Raises:
            PermissionError: The operation is prohibited.
        """
        raise PermissionError("Operation prohibited.")

    def initialize_transfer(self) -> None:
        """
        Would normally open the target file, but here is prohibited.

        Raises:
            PermissionError: The operation is prohibited.
        """

        raise PermissionError("Operation prohibited.")


class TFTPServerProtocol(py3tftp.protocols.BaseTFTPServerProtocol):
    """
    TFTP server implementation with only write capabilities.

    The server implementation sends a data_directory argument
    to the writing handler, specifying where to stash files
    while also prohibiting read operations.

    Attributes:
        data_directory: Path to the data directory.
    """

    __slots__: tuple[str, ...] = ("data_directory",)

    def __init__(
        self, *args, data_directory: pathlib.Path = pathlib.Path("data"), **kwargs
    ):
        """
        Initializes the TFTP server.

        Args:
            *args: Arguments - see parent class.
            data_directory: Path to the data directory.
            **kwargs: Keyword arguments - see parent class.
        """
        super().__init__(*args, **kwargs)
        self.data_directory = data_directory

    def select_protocol(
        self, request: py3tftp.tftp_packet.TFTPRequestPacket
    ) -> type[py3tftp.protocols.BaseTFTPProtocol]:
        """
        Determines the appropriate protocol handler.

        Restricts the request to write-only.

        Args:
            request: The initial packet.

        Returns:
            The appropriate protocol handler.
        """

        logger.debug("Packet type: %s", request.pkt_type)
        if request.is_wrq():
            return py3tftp.protocols.WRQProtocol

        return OperationProhibitedProtocol

    def select_file_handler(
        self, first_packet: py3tftp.tftp_packet.TFTPRequestPacket
    ) -> Callable[[bytes, int], object]:
        """
        Provides an appropriate file handler based on the initial packet.

        Args:
            first_packet: The initial packet.

        Returns:
            A callable accepting the file name and mode returning a file
            handler. Will only ever provide a valid handler given a
            writing request.
        """

        if first_packet.is_wrq():
            return lambda filename, opts: stashhouse_tftp.file_io.FileWriter(
                filename, opts, first_packet.mode, data_directory=self.data_directory
            )

        return lambda filename, opts: ...


__all__: tuple[str, ...] = ("TFTPServerProtocol",)
