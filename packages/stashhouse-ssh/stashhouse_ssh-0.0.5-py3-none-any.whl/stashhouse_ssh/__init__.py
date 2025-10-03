# Copyright (c) 2025 Jayson Fong
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
SSH-based file transfer protocol implementations.

Implementation of a Secure Copy Protocol (SCP) and
Secure File Transfer Protocol (SFTP) server.
"""
import argparse
import asyncio
import functools
import logging
import multiprocessing
import os
from typing import TYPE_CHECKING

import asyncssh
import asyncssh.misc
from asyncssh import SSHServerConnectionOptions

from . import connection, sftp

if TYPE_CHECKING:
    from stashhouse import server
    from stashhouse import plugin

__version__: str = "0.0.5"
logger = logging.getLogger(__name__)


class _SSHServer(asyncssh.SSHServer):
    """
    Secure Shell (SSH) server without authentication.
    """

    def connection_made(self, conn) -> None:
        # noinspection SpellCheckingInspection
        remote_host, remote_port = conn.get_extra_info("peername")
        logger.info("Connection received from %s:%s", remote_host, remote_port)

    # noinspection PyUnusedLocal
    def begin_auth(self, username: str) -> bool:
        """
        The client has requested authentication.

        Indicates that authentication is never required for any client.

        Args:
            username: Name of the user being authenticated.

        Returns:
            A `bool` indicating whether authentication is required.
        """

        del username
        return False


# pylint: disable=too-few-public-methods
class SSHServer:
    """
    Plugin to accept files over SSH-based protocols without authentication.

    Attributes:
        server_options: Server options applied globally.
        exited: Whether shutdown should be performed.
        port: Port to listen on.
        host_key: SSH host key.
    """

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(
        self,
        server_options: "server.ServerOptions",
        exited: multiprocessing.Event,
        port: int = 22,
        host_key_file: str | None = None,
        save_host_key: bool = True,
    ):
        """
        Initialize the SSH server.

        Args:
            server_options: Server options applied globally.
            exited: Whether shutdown should be performed.
            port: Port to listen on.
            host_key_file: File path to load the host key from.
            save_host_key: If the host key file does not exist, whether to save one.
        """

        self.server_options = server_options
        self.exited = exited
        self.port = port

        if host_key_file:
            self.host_key = host_key_file
            self._check_host_key(save_host_key)
        else:
            self.host_key = asyncssh.generate_private_key("ssh-rsa")

    def _check_host_key(self, save_host_key: bool = True) -> None:
        """
        Check if the host key is valid and generate one if needed

        If a host key file path is set but the file does not exist,
        generates a new SSH-RSA key and saves it at the specified path

        :param save_host_key: Whether to save the host key to the specified file
        """
        if isinstance(self.host_key, str) and not os.path.isfile(self.host_key):
            if not save_host_key:
                raise RuntimeError(
                    f"The specified host key file does not exist, "
                    f"but host key saving is disabled: {self.host_key}"
                )

            asyncssh.generate_private_key("ssh-rsa").write_private_key(self.host_key)

    async def _run(self) -> None:
        """
        Starts the SSH server.

        Every second, the `exited` attribute is checked
        to determine whether the server should stop.
        """

        ssh_server = await connection.listen(
            self.server_options.host,
            self.port,
            allow_scp=True,
            server_host_keys=[self.host_key],
            server_factory=_SSHServer,
            sftp_factory=functools.partial(
                sftp.SFTPServer, directory=self.server_options.directory
            ),
            options=SSHServerConnectionOptions(
                server_version=f"StashHouseSSH_{__version__}"
            ),
        )

        for address, port in ssh_server.get_addresses():
            logger.info("Started SSH server on %s:%d", address, port)

        while not self.exited.is_set():
            await asyncio.sleep(1.0)

        logger.info("Stopping server")
        ssh_server.close()
        await ssh_server.wait_closed()

    def run(self) -> None:
        """
        Executes the SSH server using asyncio.
        """

        asyncio.run(self._run())

    @classmethod
    def register_arguments(
        cls, plugin_name: str, parser: argparse.ArgumentParser
    ) -> None:
        """
        Adds arguments to a parser for a plugin.

        Args:
            plugin_name: The plugin name.
            parser: An argument parser.
        """

        # fmt: off
        group = parser.add_argument_group(
            "Secure Shell",
            description="Secure Copy Protocol (SCP) and Secure "
                        "File Transfer Protocol (SFTP) server options",
        )
        # If a port is not specified, one will be automatically
        # determined, although it will perhaps be unexpected.
        # fmt: off
        group.add_argument(
            f"--{plugin_name}.port",
            type=int, dest=f"{plugin_name}.port",
            help="Port to listen on"
        )

        # SSH host key file
        # fmt: off
        group.add_argument(
            f"--{plugin_name}.host-key-file",
            dest=f"{plugin_name}.host_key_file",
            help="SSH host key file path"
        )
        # fmt: off
        group.add_argument(
            f"--{plugin_name}.disable-host-key-save",
            default=True, action="store_false", dest=f"{plugin_name}.save_host_key",
            help="If a host key file is set and does not exist, do not save a new one and abort"
        )

    @classmethod
    def derive_options(
        cls, plugin_name: str, args: argparse.Namespace
    ) -> "stashhouse.plugin.PluginOptions":
        """
        Given a namespace, extracts the plugin's options.

        Args:
            plugin_name: The plugin name.
            args: An argument parser.

        Returns:
            A dictionary of values for the plugin.
        """

        return {
            "port": getattr(args, f"{plugin_name}.port", 22),
            "host_key_file": getattr(args, f"{plugin_name}.host_key_file", None),
            "save_host_key": getattr(args, f"{plugin_name}.save_host_key", True),
        }


__all__ = ("SSHServer",)
