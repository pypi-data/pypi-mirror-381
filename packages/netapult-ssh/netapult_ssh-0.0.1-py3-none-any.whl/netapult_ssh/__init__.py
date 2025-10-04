import os
from typing import Iterable, Any

import netapult.channel
import paramiko


class SSHChannel(netapult.channel.Channel):

    def __init__(
        self,
        protocol_name: str,
        host: str,
        port: int = 22,
        username: str | None = None,
        password: str | None = None,
        read_buffer_size: int = 1024,
        read_max_buffer_size: int = 65535,
        read_max_loops: int = -1,
        load_system_host_keys: bool = True,
        host_key_files: Iterable[str] | None = None,
        ssh_strict: bool = False,
        auth_timeout: float = 10.0,
        banner_timeout: float = 10.0,
        timeout: float = 10.0,
        terminal_type: str = "vt100",
        terminal_height: int = 1024,
        terminal_width: int = 1024,
    ):
        super().__init__(protocol_name)

        self.host: str = host
        self.port: int = port
        self.username: str | None = username
        self.password: str | None = password

        self.read_buffer_size: int = read_buffer_size
        self.read_max_buffer_size: int = read_max_buffer_size
        self.read_max_loops: int = read_max_loops

        self.load_system_host_keys: bool = load_system_host_keys
        self.host_key_files: Iterable[str] | None = host_key_files

        self.ssh_strict = ssh_strict

        self.auth_timeout: float = auth_timeout
        self.banner_timeout: float = banner_timeout
        self.timeout: float = timeout

        self.terminal_type: str = terminal_type
        self.terminal_height: int = terminal_height
        self.terminal_width: int = terminal_width

        self.remote_client: paramiko.SSHClient | None = None
        self.remote_connection: paramiko.Channel | None = None

    def read(
        self,
        buffer_size: int | None = None,
        max_size: int | None = None,
        max_loops: int | None = None,
    ) -> bytes:
        if not self.remote_connection:
            raise RuntimeError("Attempted to read, but there is no active channel")

        buffer_size = buffer_size or self.read_buffer_size
        max_size = max_size or self.read_max_buffer_size
        max_loops = max_loops or self.read_max_loops

        output_buffer: bytes = b""
        loops: int = 0
        while (max_loops == -1 or loops < max_loops) and (
            max_size is None or len(output_buffer) < max_size
        ):
            if not self.remote_connection.recv_ready():
                return output_buffer

            buffer: bytes = self.remote_connection.recv(min(buffer_size, max_size))
            if len(buffer) == 0:
                raise RuntimeError("Channel stream has closed")

            output_buffer += buffer
            loops += 1

        return output_buffer

    def write(self, payload: bytes) -> None:
        if not self.remote_connection:
            raise RuntimeError("Attempted to write, but there is no active channel")

        self.remote_connection.sendall(payload)

    def connect(self) -> None:
        self._create_ssh_client()

    def disconnect(self) -> None:
        if self.remote_connection:
            self.remote_connection.close()

        if self.remote_client:
            self.remote_client.close()

    def _create_ssh_client(self):
        self.remote_client = paramiko.SSHClient()
        if self.load_system_host_keys:
            self.remote_client.load_system_host_keys()

        if self.host_key_files:
            for host_key_file in self.host_key_files:
                if not os.path.isfile(host_key_file):
                    self.remote_client.load_host_keys(host_key_file)

        host_key_policy: paramiko.MissingHostKeyPolicy
        if self.ssh_strict:
            host_key_policy = paramiko.RejectPolicy()
        else:
            host_key_policy = paramiko.AutoAddPolicy()

        self.remote_client.set_missing_host_key_policy(host_key_policy)

        self.remote_client.connect(**self._paramiko_connect_params())

        self.remote_connection = self.remote_client.invoke_shell(
            term=self.terminal_type,
            height=self.terminal_height,
            width=self.terminal_width,
        )

    def _paramiko_connect_params(self) -> dict[str, Any]:
        return {
            "hostname": self.host,
            "username": self.username,
            "password": self.password,
            "auth_timeout": self.auth_timeout,
            "banner_timeout": self.banner_timeout,
            "timeout": self.timeout,
        }
