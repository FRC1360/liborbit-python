import ipaddress
from socket import socket, AF_INET, SOCK_DGRAM
from typing import Callable, Any


class UdpTranceiver:
    def __init__(self, local_port: int, local_address: ipaddress, remote_port: int, remote_address: ipaddress) -> None:
        super().__init__()
        self.local_port = local_port
        self.local_address = local_address
        self.remote_port = remote_port
        self.remote_address = remote_address
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((local_address, local_port))

    def __str__(self) -> str:
        return "%s from %s:%d to %s:%d" % (self.__class__.__name__, str(self.local_address), self.local_port,
                                           str(self.remote_address), self.remote_port)

    def send(self, data: bytes, **kwargs) -> None:
        self.socket.sendto(data, (self.remote_address, self.remote_port))

    def recv(self) -> bytes:
        return self.socket.recv(65535)

    def recv_all(self, callback: Callable[[Any], None]):
        while True:
            callback(self.recv())


class UdpMultiChannelTranceiver(UdpTranceiver):
    def __init__(self, local_port: int, local_address: ipaddress, remote_port: int, remote_address: ipaddress) -> None:
        super().__init__(local_port, local_address, remote_port, remote_address)

    def send(self, data: bytes, **kwargs) -> None:
        if 'channel' not in kwargs:
            raise Exception('Missing named argument "channel"')
        if len(data) > 65534:
            raise Exception('Data payload cannot be longer than 65534 bytes')
        super().send(bytes([kwargs['channel']]) + data)

    def recv(self) -> (int, bytes):
        data = super().recv()
        if len(data) < 1:
            raise Exception('Empty datagram')
        return int(data[0]), data[1:]
