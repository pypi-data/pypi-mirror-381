# kn_sock/udp.py

import socket
import asyncio
from typing import Callable, Awaitable

BUFFER_SIZE = 1024


def _get_socket_family(host):
    # Return AF_INET6 if host is IPv6, else AF_INET
    if ":" in host:
        return socket.AF_INET6
    return socket.AF_INET


# -----------------------------
# 📥 Sync UDP Server
# -----------------------------


def start_udp_server(
    port: int,
    handler_func: Callable[[bytes, tuple, socket.socket], None],
    host: str = "0.0.0.0",
    shutdown_event=None,
):
    """
    Starts a synchronous UDP server (IPv4/IPv6 supported) with graceful shutdown support.
    Args:
        port (int): Port to bind.
        handler_func (callable): Function to handle (data, addr, socket).
        host (str): Host to bind (IPv4 or IPv6).
        shutdown_event (threading.Event, optional): If provided, server will exit when event is set.
    """
    family = _get_socket_family(host)
    server_socket = socket.socket(family, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"[UDP][SYNC] Server listening on {host}:{port}")

    while True:
        if shutdown_event is not None and shutdown_event.is_set():
            print("[UDP][SYNC] Shutdown event set. Stopping UDP server.")
            break
        server_socket.settimeout(1.0)
        try:
            data, addr = server_socket.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            continue
        handler_func(data, addr, server_socket)
    server_socket.close()


# -----------------------------
# 📤 Sync UDP Client
# -----------------------------


def send_udp_message(host: str, port: int, message: str):
    """
    Sends a message to a UDP server (IPv4/IPv6 supported).
    """
    family = _get_socket_family(host)
    with socket.socket(family, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode("utf-8"), (host, port))
        print(f"[UDP][SYNC] Sent to {host}:{port}")


# -----------------------------
# 📥 Async UDP Server
# -----------------------------


async def start_udp_server_async(
    port: int,
    handler_func: Callable[[bytes, tuple, asyncio.DatagramTransport], Awaitable[None]],
    host: str = "0.0.0.0",
    shutdown_event=None,
):
    """
    Starts an asynchronous UDP server with graceful shutdown support.
    Args:
        port (int): Port to bind.
        handler_func (callable): async function (data, addr, transport).
        host (str): Host to bind.
        shutdown_event (asyncio.Event, optional): If provided, server will exit when event is set.
    """

    class UDPProtocol(asyncio.DatagramProtocol):
        def __init__(self, loop):
            self.loop = loop

        def connection_made(self, transport):
            self.transport = transport
            print(f"[UDP][ASYNC] Server listening on {host}:{port}")

        def datagram_received(self, data, addr):
            asyncio.create_task(handler_func(data, addr, self.transport))

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPProtocol(loop), local_addr=(host, port)
    )
    try:
        if shutdown_event is not None:
            await shutdown_event.wait()
            print("[UDP][ASYNC] Shutdown event set. Stopping async UDP server.")
        else:
            while True:
                await asyncio.sleep(3600)  # Run forever
    finally:
        transport.close()
        print("[UDP][ASYNC] Async UDP server shutdown complete.")


# -----------------------------
# 📤 Async UDP Client
# -----------------------------


async def send_udp_message_async(host: str, port: int, message: str):
    """
    Sends a message to a UDP server asynchronously.
    """
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        lambda: asyncio.DatagramProtocol(), remote_addr=(host, port)
    )
    transport.sendto(message.encode("utf-8"))
    print(f"[UDP][ASYNC] Sent to {host}:{port}")
    transport.close()


def send_udp_multicast(group: str, port: int, message: str, ttl: int = 1):
    """
    Send a UDP multicast message to the given group and port.
    Args:
        group (str): Multicast group IP (e.g., '224.0.0.1').
        port (int): Multicast port.
        message (str): Message to send.
        ttl (int): Multicast TTL (default 1).
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.sendto(message.encode("utf-8"), (group, port))
    sock.close()


def start_udp_multicast_server(
    group: str,
    port: int,
    handler_func: Callable[[bytes, tuple, socket.socket], None],
    listen_ip: str = "0.0.0.0",
    shutdown_event=None,
):
    """
    Start a UDP multicast server that listens for messages on the given group and port.
    Args:
        group (str): Multicast group IP (e.g., '224.0.0.1').
        port (int): Multicast port.
        handler_func (callable): Function to handle (data, addr, socket).
        listen_ip (str): Local IP to bind (default '0.0.0.0').
        shutdown_event (threading.Event, optional): For graceful shutdown.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((listen_ip, port))
    mreq = socket.inet_aton(group) + socket.inet_aton(listen_ip)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print(f"[UDP][MULTICAST] Listening on group {group}:{port}")
    try:
        while True:
            if shutdown_event is not None and shutdown_event.is_set():
                print("[UDP][MULTICAST] Shutdown event set. Stopping multicast server.")
                break
            sock.settimeout(1.0)
            try:
                data, addr = sock.recvfrom(BUFFER_SIZE)
            except socket.timeout:
                continue
            handler_func(data, addr, sock)
    finally:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
        sock.close()
        print("[UDP][MULTICAST] Multicast server shutdown complete.")
