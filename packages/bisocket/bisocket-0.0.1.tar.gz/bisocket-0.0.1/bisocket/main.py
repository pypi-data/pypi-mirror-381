import os
import bz2
import uuid
import time
import json
import socket
import inspect
import asyncio
import traceback
import threading
import queue
from typing import Callable
from dataclasses import dataclass

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


VERSION = '0.0.0'
END_TOKEN = b'|[-_-]|'
SPLIT_TOKEN = b'|(---)|'
SPLIT_TOKEN2 = b'|{***}|'
LENGTH_OF_END_TOKEN = len(END_TOKEN)


def receive(conn: socket.socket) -> bytes:
    data = b''
    while not data.endswith(END_TOKEN):
        v = conn.recv(1024)
        if not v:
            # If the connection is closed, we'll break out of the loop
            break
        data += v

    if not data.endswith(END_TOKEN):
        # If we broke out of the loop and don't have the end token,
        # it means the connection was closed prematurely.
        try:
            decoded_data = data.decode()
        except UnicodeDecodeError:
            decoded_data = repr(data)
        
        return decoded_data
        raise ValueError(f'Invalid value received: `{decoded_data}`')

    return data[:-LENGTH_OF_END_TOKEN]


def send(conn: socket.socket, data: bytes) -> None:
    conn.sendall(data+END_TOKEN)


async def async_receive(sock: socket.socket) -> bytes | str:
    loop = asyncio.get_running_loop()
    data = b''

    while not data.endswith(END_TOKEN):
        chunk = await loop.sock_recv(sock, 1024)
        if not chunk:  # connection closed
            try:
                return data.decode()
            except UnicodeDecodeError:
                return repr(data)
        data += chunk

    return data[:-LENGTH_OF_END_TOKEN]


async def async_send(sock: socket.socket, data: bytes) -> None:
    loop = asyncio.get_running_loop()
    await loop.sock_sendall(sock, data + END_TOKEN)


def compress_bytes(data):
    return bz2.compress(data, compresslevel=9)


def decompress_bytes(data):
    return bz2.decompress(data)


@dataclass
class CompressedEncryptedData:
    data: bytes
    iv: bytes

    def to_dict(self) -> dict:
        return {
            'data': list(self.data),  # .hex(),
            'iv': list(self.iv),  # .hex(),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
    def to_bytes(self) -> bytes:
        return compress_bytes(self.to_json().encode())
    
    @classmethod
    def from_dict(cls, data: dict) -> 'CompressedEncryptedData':
        return cls(
            data=bytes(data['data']),
            iv=bytes(data['iv']),
        )
    
    @classmethod
    def from_json(cls, data: str) -> 'CompressedEncryptedData':
        return cls.from_dict(json.loads(data))
    
    def encrypted_data(self) -> 'EncryptedData':
        return EncryptedData(
            data=decompress_bytes(self.data),
            iv=decompress_bytes(self.iv),
        )
    

@dataclass
class EncryptedData:
    data: bytes
    iv: bytes

    def to_dict(self) -> dict:
        return {
            'data': list(self.data),  # .hex(),
            'iv': list(self.iv),  # .hex(),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
    def to_bytes(self) -> bytes:
        return compress_bytes(SPLIT_TOKEN2.join([self.data, self.iv]))
    
    @classmethod
    def from_dict(cls, data: dict) -> 'EncryptedData':
        return cls(
            data=bytes(data['data']),
            iv=bytes(data['iv']),
        )
    
    @classmethod
    def from_json(cls, data: str) -> 'EncryptedData':
        return cls.from_dict(json.loads(data))
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'EncryptedData':
        data, iv = decompress_bytes(data).split(SPLIT_TOKEN2)
        return cls(
            data=data,
            iv=iv,
        )
    
    def compress_data(self) -> 'CompressedEncryptedData':
        return CompressedEncryptedData(
            data=compress_bytes(self.data),
            iv=compress_bytes(self.iv),
        )

    @classmethod
    def decompress_data(cls, data: 'CompressedEncryptedData') -> 'EncryptedData':
        return EncryptedData(
            data=decompress_bytes(data.data),
            iv=decompress_bytes(data.iv),
        )


class EncryptionService:
    def __init__(self, key_string: str):
        self.key = self.derive_key(key_string)
        self.aesgcm = AESGCM(self.key)

    @staticmethod
    def derive_key(key_string: str) -> bytes:
        """Derive a 32-byte key from the input string using SHA-256"""
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(key_string.encode())
        return digest.finalize()

    def encrypt_obj(self, obj: dict) -> EncryptedData:
        """Encrypt data using AES-GCM"""
        # Convert data to JSON string and encode
        data_bytes = json.dumps(obj).encode()

        return self.encrypt_data(data_bytes)

    def decrypt_obj(self, encrypted: bytes, iv: bytes) -> dict:
        """Decrypt data using AES-GCM"""
        return json.loads(self.decrypt_data(encrypted, iv).decode())

    def encrypt_data(self, data: bytes) -> EncryptedData:
        """Encrypt data using AES-GCM"""
        # Generate 12-byte IV
        iv = os.urandom(12)

        # Encrypt data (includes auth tag automatically)
        encrypted = self.aesgcm.encrypt(iv, data, None)

        return EncryptedData(encrypted, iv)

    def decrypt_data(self, encrypted_data: EncryptedData) -> bytes:
        """Decrypt data using AES-GCM"""
        try:
            # Decrypt data
            decrypted_bytes = self.aesgcm.decrypt(encrypted_data.iv, encrypted_data.data, None)

            # Parse JSON data
            return decrypted_bytes  # json.loads(decrypted_bytes.decode())
        except Exception as e:
            print(f"Decryption error: {str(e)}")
            raise ValueError("Failed to decrypt data")


@dataclass
class Message:
    request_id: str
    data: bytes


class Client:
    def __init__(
            self, 
            host: str, 
            port: int, 
            on_receive: callable,
        ) -> None:
        # Initialize encryption service
        self.client_id = str(uuid.uuid4())

        crypto_key = os.environ.get('CRYPTO_KEY', 'secret-lol')
        self.encryption_service = EncryptionService(crypto_key)

        self.host = host
        self.port = port

        self.on_receive = on_receive
        self.receive_queue = queue.Queue()
        self.areceive_queue = asyncio.Queue()

        self.send_conn: socket.socket | None = None
        self.receive_conn: socket.socket | None = None

        self.receiving = False
        self.receiving_thread: threading.Thread | None = None
        self._receiving_thread: threading.Thread | None = None

        self.receiving_task: threading.Thread | None = None
        self._receiving_task: asyncio.Task | None = None

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def encrypt(self, data: bytes) -> bytes:
        return self.encryption_service.encrypt_data(data).to_bytes()
    
    def decrypt(self, data: bytes) -> bytes:
        encrypted_data: EncryptedData = EncryptedData.from_bytes(data)
        return self.encryption_service.decrypt_data(encrypted_data)

    def send(self, method: str, data: bytes) -> str:
        request_id = str(uuid.uuid4())
        send(self.send_conn, self.encrypt(SPLIT_TOKEN.join([method.encode(), request_id.encode(), data])))
        receive(self.send_conn)
        return request_id

    def __receive_thread(self) -> bytes:
        while self.receiving:
            try:
                while (data := self.receive_queue.get()) is not None:
                    if data:
                        request_id, data = self.decrypt(data).split(SPLIT_TOKEN)

                        if data == b'__close__':
                            # print('close!', request_id, data)
                            break

                        msg = Message(request_id.decode(), data)
                        self.on_receive(msg)
            except Exception as e:
                print(f'Error receiving data: {e}')
                traceback.print_exc()
                break
    
    def _receive_thread(self) -> bytes:
        while self.receiving:
            try:
                data = receive(self.receive_conn)
                if data:
                    self.receive_queue.put(data)
                    # request_id, data = self.decrypt(data).split(SPLIT_TOKEN)

                    # if data == b'__close__':
                    #     print('close!', request_id, data)
                    #     break

                    # msg = Message(request_id.decode(), data)
                    # self.on_receive(msg)
            except Exception as e:
                print(f'Error receiving data: {e}')
                traceback.print_exc()
                break
        self.receive_queue.put(None)
    
    def open(self) -> None:
        # Send the client ID to the server
        # self.send(self.client_id.encode())

        self.receive_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.receive_conn.connect((self.host, self.port))

        send(self.receive_conn, self.encrypt(SPLIT_TOKEN.join([b'receive', self.client_id.encode()])))
        assert b'ok' == self.decrypt(receive(self.receive_conn))

        # Start the receive thread
        self.receiving = True
        self.receiving_thread = threading.Thread(target=self._receive_thread, daemon=True)
        self.receiving_thread.start()
        self._receiving_thread = threading.Thread(target=self.__receive_thread, daemon=True)
        self._receiving_thread.start()

        self.send_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.send_conn.connect((self.host, self.port))

        send(self.send_conn, self.encrypt(SPLIT_TOKEN.join([b'send', self.client_id.encode()])))
        assert b'ok' == self.decrypt(receive(self.send_conn))

    def close(self) -> None:
        self.send('close', b'closing')
        assert self.decrypt(self.server_receive(self.send_conn)) == b'__close__'
        self.send_conn.close()

        self.receiving = False
        if self.receiving_thread:
            self.receiving_thread.join()
            self.receiving_thread = None

        if self._receive_thread:
            self._receiving_thread.join()
            self._receiving_thread = None
            
        self.receive_conn.close()
    
    def server_receive(self, s):
        while not (data := receive(s)):
            pass
        return data

    async def __aenter__(self):
        await self.aopen()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    async def aencrypt(self, data: bytes) -> bytes:
        # return self.encryption_service.encrypt_data(data).to_bytes()
        return await asyncio.to_thread(self.encrypt, data)
    
    async def adecrypt(self, data: bytes) -> bytes:
        # data = EncryptedData.from_bytes(data)
        # return self.encryption_service.decrypt_data(data)
        return await asyncio.to_thread(self.decrypt, data)

    async def asend(self, method: str, data: bytes) -> str:
        request_id = str(uuid.uuid4())
        await async_send(self.send_conn, await self.aencrypt(SPLIT_TOKEN.join([method.encode(), request_id.encode(), data])))
        await async_receive(self.send_conn)
        return request_id

    async def __areceive_thread(self) -> bytes:
        while self.receiving:
            try:
                while (data := await self.areceive_queue.get()) is not None:
                    if data:
                        request_id, data = (await self.adecrypt(data)).split(SPLIT_TOKEN)

                        if data == b'__close__':
                            # print('close!', request_id, data)
                            break

                        msg = Message(request_id.decode(), data)
                        
                        if inspect.iscoroutinefunction(self.on_receive):
                            await self.on_receive(msg)
                        else:
                            # self.on_receive(msg)
                            await asyncio.to_thread(self.on_receive, msg)
            except Exception as e:
                print(f'Error receiving data: {e}')
                traceback.print_exc()
                break
    
    def _areceive_thread(self) -> bytes:
        while self.receiving:
            try:
                data = receive(self.receive_conn)
                if data:
                    self.areceive_queue.put_nowait(data)
                    # request_id, data = self.decrypt(data).split(SPLIT_TOKEN)

                    # if data == b'__close__':
                    #     print('close!', request_id, data)
                    #     break

                    # msg = Message(request_id.decode(), data)
                    # self.on_receive(msg)
            except Exception as e:
                print(f'Error receiving data: {e}')
                traceback.print_exc()
                break
        self.areceive_queue.put_nowait(None)
    
    async def aopen(self) -> None:
        loop = asyncio.get_running_loop()

        def receive_socket_setup():
            self.receive_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.receive_conn.setblocking(False)
            self.receive_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            # await loop.sock_connect(self.receive_conn, (self.host, self.port))
            self.receive_conn.connect((self.host, self.port))

            # await async_send(self.receive_conn, await self.aencrypt(SPLIT_TOKEN.join([b'receive', self.client_id.encode()])))
            # assert b'ok' == await self.adecrypt(await async_receive(self.receive_conn))
            send(self.receive_conn, self.encrypt(SPLIT_TOKEN.join([b'receive', self.client_id.encode()])))
            assert b'ok' == self.decrypt(receive(self.receive_conn))
        
        await asyncio.to_thread(receive_socket_setup)

        # Start the receive thread
        self.receiving = True
        self.receiving_task = threading.Thread(target=self._areceive_thread, daemon=True)  # asyncio.create_task(self._areceive_thread())
        self.receiving_task.start()
        self._receiving_task = asyncio.create_task(self.__areceive_thread())
        # self._receiving_task.start()

        self.send_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_conn.setblocking(False)
        self.send_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        await loop.sock_connect(self.send_conn, (self.host, self.port))
        # self.send_conn.connect((self.host, self.port))

        await async_send(self.send_conn, await self.aencrypt(SPLIT_TOKEN.join([b'send', self.client_id.encode()])))
        assert b'ok' == await self.adecrypt(await async_receive(self.send_conn))

    async def aclose(self) -> None:
        await self.asend('close', b'closing')
        assert (await self.adecrypt(await self.aserver_receive(self.send_conn))) == b'__close__'
        self.send_conn.close()

        self.receiving = False
        if self.receiving_task:
            self.receiving_task.join()
            self.receiving_task = None

        if self._receiving_task:
            await self._receiving_task
            self._receiving_task = None

        self.receive_conn.close()
    
    async def aserver_receive(self, s):
        while not (data := await async_receive(s)):
            pass
        return data


@dataclass
class ServerRequest:
    method: str
    data: bytes
    send_data: Callable[[bytes], None]


class Server:
    def __init__(self, host: str, port: int, handler: Callable[[ServerRequest], None]):
        self.host = host
        self.port = port
        self.handler = handler

        self.client_queue: list[str, queue.Queue | asyncio.Queue] = {}
        self.client_send_socket: list[str, queue.Queue] = {}

        crypto_key = os.environ.get('CRYPTO_KEY', 'secret-lol')
        self.encryption_service = EncryptionService(crypto_key)

    def encrypt(self, data: bytes) -> bytes:
        return self.encryption_service.encrypt_data(data).to_bytes()
    
    def decrypt(self, data: bytes) -> bytes:
        encrypted_data: EncryptedData = EncryptedData.from_bytes(data)
        return self.encryption_service.decrypt_data(encrypted_data)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            attempts = 5
            for attempt in range(1, attempts + 1):
                try:
                    server.bind((self.host, self.port))
                    break
                except OSError:
                    print(f"Port {self.port} is already in use. Retrying...")
                    time.sleep(5 * attempt)
                    if attempt == attempts:
                        raise
            server.listen()
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                client_socket, addr = server.accept()
                print(f"Connection from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True)
                client_thread.start()
        finally:
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            exit()
    
    def server_receive(self, s):
        while not (data := receive(s)):
            pass
        return data
    
    def handle_requests(self, s, q: queue.Queue, request_q: queue.Queue, loop=None):
        method, request_id, data = self.decrypt(self.server_receive(s)).split(SPLIT_TOKEN)
        send(s, b'ok')

        while method != b'close':
            def get_send_data_func(req_id: bytes):
                def send_data(data: bytes) -> None:
                    q.put_nowait(SPLIT_TOKEN.join([req_id, data]))
                return send_data
                
            request_q.put_nowait(
                ServerRequest(
                    method.decode(), 
                    data, 
                    get_send_data_func(request_id)
                )
            )
            # self.handler(ServerRequest(method.decode(), data, send_data))
            method, request_id, data = self.decrypt(self.server_receive(s)).split(SPLIT_TOKEN)
            send(s, b'ok')
        
        if loop:
            loop.call_soon_threadsafe(request_q.put_nowait, None)
        else:
            request_q.put_nowait(None)
        
        
    def handle_client(self, s):
        with s:
            client_type, client_id = self.decrypt(receive(s)).split(SPLIT_TOKEN)
            client_id = client_id.decode()

            if client_type == b'send':
                request_q: queue.Queue = queue.Queue()
                
                q: queue.Queue = queue.Queue()
                self.client_queue[client_id] = q
                self.client_send_socket[client_id] = s

                send(s, self.encrypt(b'ok'))

                # method, request_id, data = self.decrypt(self.server_receive(s)).split(SPLIT_TOKEN)
                # while method != b'close':
                #     def send_data(data: bytes) -> None:
                #         q.put(SPLIT_TOKEN.join([request_id, data]))
                #     self.handler(ServerRequest(method.decode(), data, send_data))
                #     method, request_id, data = self.decrypt(self.server_receive(s)).split(SPLIT_TOKEN)

                t = threading.Thread(target=self.handle_requests, args=(s, q, request_q), daemon=True)
                t.start()

                while (request := request_q.get()) is not None:
                    request: ServerRequest
                    # print('handling', request)
                    self.handler(request)

                q.put(b'close')
                while client_id in self.client_send_socket:
                    time.sleep(1.0)
            elif client_type == b'receive':
                send(s, self.encrypt(b'ok'))

                t = time.time()
                while client_id not in self.client_queue:
                    time.sleep(0.1)
                    if time.time() - t > 60:
                        raise ValueError('Timeout waiting for client queue')
                
                q: queue.Queue = self.client_queue[client_id]

                while (data := q.get()) != b'close':
                    if data:
                        send(s, self.encrypt(data))
                        
                send(s, self.encrypt(SPLIT_TOKEN.join([b'empty-id', b'__close__'])))
                
                del self.client_queue[client_id]
                send(self.client_send_socket[client_id], self.encrypt(b'__close__'))
                del self.client_send_socket[client_id]
                time.sleep(1.0)
            # method, data = receive(s).split(SPLIT_TOKEN)

    async def aencrypt(self, data: bytes) -> bytes:
        return await asyncio.to_thread(self.encrypt, data)
    
    async def adecrypt(self, data: bytes) -> bytes:
        return await asyncio.to_thread(self.decrypt, data)

    async def astart(self):
        loop = asyncio.get_running_loop()

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setblocking(False)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # await loop.sock_accept(self.send_conn, (self.host, self.port))

        try:
            attempts = 5
            for attempt in range(1, attempts + 1):
                try:
                    server.bind((self.host, self.port))
                    break
                except OSError:
                    print(f"Port {self.port} is already in use. Retrying...")
                    await asyncio.sleep(5 * attempt)
                    if attempt == attempts:
                        raise
            server.listen()
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                client_socket, addr = await loop.sock_accept(server)  # server.accept()
                print(f"Connection from {addr}")
                # client_thread = threading.Thread(target=self.ahandle_client, args=(client_socket,), daemon=True)
                # client_thread.start()
                client_socket.setblocking(False)
                asyncio.create_task(self.ahandle_client(client_socket))
        finally:
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            exit()
    
    async def aserver_receive(self, s):
        while not (data := await async_receive(s)):
            pass
        return data
    
    async def ahandle_requests(self, s, q: asyncio.Queue, request_q: asyncio.Queue):
        method, request_id, data = (await self.adecrypt(await self.aserver_receive(s))).split(SPLIT_TOKEN)

        while method != b'close':
            # async def send_data(data: bytes) -> None:
            #     await q.put(SPLIT_TOKEN.join([request_id, data]))
            def get_send_data_func(req_id: bytes):
                def send_data(data: bytes) -> None:
                    q.put_nowait(SPLIT_TOKEN.join([req_id, data]))
                return send_data
                
            await request_q.put(ServerRequest(method.decode(), data, get_send_data_func(request_id)))
            # self.handler(ServerRequest(method.decode(), data, send_data))
            method, request_id, data = (await self.adecrypt(await self.aserver_receive(s))).split(SPLIT_TOKEN)
        
        await request_q.put(None)
        
        
    async def ahandle_client(self, s: socket.socket):
        with s:
            client_type, client_id = (await self.adecrypt(await async_receive(s))).split(SPLIT_TOKEN)
            client_id = client_id.decode()

            if client_type == b'send':
                request_q: asyncio.Queue = asyncio.Queue()
                
                q: asyncio.Queue = asyncio.Queue()
                self.client_queue[client_id] = q
                self.client_send_socket[client_id] = s

                await async_send(s, self.encrypt(b'ok'))

                s.setblocking(True)
                t = threading.Thread(target=self.handle_requests, args=(s, q, request_q, asyncio.get_running_loop()), daemon=True)
                t.start()
                # asyncio.create_task(self.ahandle_requests(s, q, request_q))

                while (request := await request_q.get()) is not None:
                    request: ServerRequest
                    print('handling', request)
                    # self.handler(request)
                    if inspect.iscoroutinefunction(self.handler):
                        await self.handler(request)
                    else:
                        await asyncio.to_thread(self.handler, request)
                
                await q.put(b'close')
                while client_id in self.client_send_socket:
                    await asyncio.sleep(1.0)
            elif client_type == b'receive':
                await async_send(s, await self.aencrypt(b'ok'))

                t = time.time()
                while client_id not in self.client_queue:
                    await asyncio.sleep(0.1)
                    if time.time() - t > 60:
                        raise ValueError('Timeout waiting for client queue')
                
                q: asyncio.Queue = self.client_queue[client_id]

                while (data := await q.get()) != b'close':
                    if data:
                        await async_send(s, await self.aencrypt(data))
                
                await async_send(s, await self.aencrypt(SPLIT_TOKEN.join([b'empty-id', b'__close__'])))
                
                del self.client_queue[client_id]
                self.client_send_socket[client_id].setblocking(False)
                await async_send(self.client_send_socket[client_id], await self.aencrypt(b'__close__'))
                del self.client_send_socket[client_id]
                await asyncio.sleep(1.0)
            # method, data = receive(s).split(SPLIT_TOKEN)


def server_handler_example(request: ServerRequest) -> None:
    if request.method == 'echo':
        request.send_data(request.data)

# # async not supported at this time
# async def aserver_handler_example(request: ServerRequest) -> None:
#     if request.method == 'echo':
#         request.send_data(request.data)

