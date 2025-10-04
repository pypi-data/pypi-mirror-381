# kn_sock/file_transfer.py

import os
import socket
import asyncio

CHUNK_SIZE = 4096

try:
    from tqdm import tqdm

    _HAS_TQDM = True
except ImportError:
    _HAS_TQDM = False


def _progress_bar(total, desc, disable=False):
    if _HAS_TQDM and not disable:
        return tqdm(total=total, unit="B", unit_scale=True, desc=desc)

    class Dummy:
        def update(self, n):
            pass

        def close(self):
            pass

    return Dummy()


# -----------------------------
# 🧱 Common Helpers
# -----------------------------


def _get_filename_from_path(path: str) -> str:
    return os.path.basename(path)


def _send_text(sock: socket.socket, text: str):
    sock.sendall((text + "\n").encode("utf-8"))


def _recv_line(sock: socket.socket) -> str:
    data = b""
    while not data.endswith(b"\n"):
        chunk = sock.recv(1)
        if not chunk:
            break
        data += chunk
    return data.decode("utf-8").strip()


async def _recv_line_async(reader: asyncio.StreamReader) -> str:
    line = await reader.readline()
    return line.decode("utf-8").strip()


# -----------------------------
# 📤 Sync File Sender
# -----------------------------


def send_file(host: str, port: int, filepath: str, show_progress: bool = True):
    filename = _get_filename_from_path(filepath)
    filesize = os.path.getsize(filepath)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        _send_text(sock, filename)
        _send_text(sock, str(filesize))

        bar = _progress_bar(filesize, f"Sending {filename}", disable=not show_progress)
        with open(filepath, "rb") as f:
            sent = 0
            while chunk := f.read(CHUNK_SIZE):
                sock.sendall(chunk)
                sent += len(chunk)
                bar.update(len(chunk))
        bar.close()


# -----------------------------
# 📥 Sync File Receiver
# -----------------------------


def start_file_server(
    port: int, save_dir: str, host: str = "0.0.0.0", show_progress: bool = True
):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[SYNC] File server listening on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"[SYNC] Connection from {addr}")

        with conn:
            filename = _recv_line(conn)
            filesize = int(_recv_line(conn))

            save_path = os.path.join(save_dir, filename)
            bar = _progress_bar(
                filesize, f"Receiving {filename}", disable=not show_progress
            )
            with open(save_path, "wb") as f:
                remaining = filesize
                while remaining > 0:
                    data = conn.recv(min(CHUNK_SIZE, remaining))
                    if not data:
                        break
                    f.write(data)
                    remaining -= len(data)
                    bar.update(len(data))
            bar.close()
            print(f"[SYNC] File saved to {save_path}")


# -----------------------------
# 📤 Async File Sender
# -----------------------------


async def send_file_async(
    host: str, port: int, filepath: str, show_progress: bool = True
):
    filename = _get_filename_from_path(filepath)
    filesize = os.path.getsize(filepath)

    reader, writer = await asyncio.open_connection(host, port)
    writer.write((filename + "\n").encode())
    writer.write((str(filesize) + "\n").encode())
    await writer.drain()

    bar = _progress_bar(filesize, f"Sending {filename}", disable=not show_progress)
    with open(filepath, "rb") as f:
        sent = 0
        while chunk := f.read(CHUNK_SIZE):
            writer.write(chunk)
            await writer.drain()
            sent += len(chunk)
            bar.update(len(chunk))
    bar.close()
    writer.close()
    await writer.wait_closed()


# -----------------------------
# 📥 Async File Receiver
# -----------------------------


async def start_file_server_async(
    port: int, save_dir: str, host: str = "0.0.0.0", show_progress: bool = True
):
    async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info("peername")
        print(f"[ASYNC] Connection from {addr}")

        try:
            filename = await _recv_line_async(reader)
            filesize = int(await _recv_line_async(reader))

            save_path = os.path.join(save_dir, filename)
            bar = _progress_bar(
                filesize, f"Receiving {filename}", disable=not show_progress
            )
            with open(save_path, "wb") as f:
                remaining = filesize
                while remaining > 0:
                    data = await reader.read(min(CHUNK_SIZE, remaining))
                    if not data:
                        break
                    f.write(data)
                    remaining -= len(data)
                    bar.update(len(data))
            bar.close()
            print(f"[ASYNC] File saved to {save_path}")

        except Exception as e:
            print(f"[ASYNC] Error: {e}")

        writer.close()
        await writer.wait_closed()

    server = await asyncio.start_server(handle_client, host, port)
    print(f"[ASYNC] File server listening on {host}:{port}...")
    async with server:
        await server.serve_forever()
