# Portions Copyright (c) 2016 Matt O. <matt@mattscodecave.com>
# Portions Copyright (c) 2025 Jayson Fong
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Utilities for file writing.

Primarily offers a wrapper around a file and enables
the customization of the data directory without
restraining the storage directory to the current
working directory.
"""

import os
import pathlib
import uuid
from typing import BinaryIO

import py3tftp.file_io
import py3tftp.netascii


# noinspection SpellCheckingInspection
def sanitize_fname(
    fname: bytes | os.PathLike[bytes], data_directory: pathlib.Path
) -> pathlib.Path:
    """
    Sanitizes the file name.

    Ensures the file name is within the defined data directory.

    Args:
        fname: Bytes of the requested file path.
        data_directory: Path to the data directory.

    Returns:
        An absolute path to store the file in.

    Raises:
        ValueError: The resolved file path is not within the defined data directory.
        FileNotFoundError: The file path is reserved.
    """

    # Remove root (/) and parent (..) directory references.
    path = os.fsdecode(fname).lstrip("./")
    abs_path = data_directory / path

    # Verify that the formed path is under the current working directory.
    try:
        abs_path.relative_to(data_directory)
    except ValueError as exc:
        raise FileNotFoundError from exc

    # Verify that we are not accessing a reserved file.
    if abs_path.is_reserved():
        raise FileNotFoundError

    return abs_path


# pylint: disable=too-few-public-methods
class FileWriter(py3tftp.file_io.FileWriter):
    # noinspection SpellCheckingInspection
    """
    Wraps around a file object.

    Given a file name, the file path is resolved to a directory
    relative to the desired data directory, if possible.

    Attributes:
        fname: Absolute path to the file being written.
        chunk_size: Minimum number of bytes written per chunk to persist.
        _f: Opened file object.
    """

    # noinspection SpellCheckingInspection
    __slots__ = ("fname", "chunk_size", "_f")

    # noinspection SpellCheckingInspection
    # pylint: disable=super-init-not-called
    def __init__(
        self,
        fname: bytes | os.PathLike[bytes],
        chunk_size,
        mode=None,
        data_directory: pathlib.Path = pathlib.Path("data").absolute(),
    ):
        """
        Initializes the wrapper.

        Automatically opens the file specified by fname.

        Args:
            fname: The requested file path.
            chunk_size: Minimum number of bytes written per chunk to persist.
            mode: File writing mode.
            data_directory: Path to the root data directory.
        """

        self._f: BinaryIO | py3tftp.netascii.Netascii | None = None
        self.fname: pathlib.Path = sanitize_fname(
            fname, data_directory.joinpath(str(uuid.uuid4()))
        )
        self.chunk_size: int = chunk_size
        self._f = self._open_file()

        if mode == b"netascii":
            self._f = py3tftp.netascii.Netascii(self._f)

    def _open_file(self) -> BinaryIO:
        """
        Creates parent directories and opens the file.

        Opens files and raises an exception if it
        already exists.

        Returns:
            A file-like object.
        """

        os.makedirs(self.fname.parent, exist_ok=True)
        return self.fname.open("xb")


__all__ = "FileWriter",
