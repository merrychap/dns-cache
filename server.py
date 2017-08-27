import abc
import sys
import socket
import struct
import select
import queue

from time import sleep
from concurrent.futures import ThreadPoolExecutor


BUFFER_SIZE = 1024
LOCAL_ADDR = ('192.0.0.8', 1027)


def get_local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(LOCAL_ADDR)
    return sock.getsockname()[0]


class BaseServer:
    def __init__(self, port):
        self._port = port

        self._sock = self._make_socket(1000000)
        self._max_workers = 5
        self._answer_queue = queue.Queue()

        print('[+] Server is configurated')

    @abc.abstractmethod
    def _client_req_handler(self, addr, packet):
        pass

    @abc.abstractmethod
    def _server_resp_handler(self, packet):
        pass

    def _make_socket(self, timeout=2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        return sock

    def shutdown(self):
        print('\n[*] Server is shutting down')
        sys.exit()

    def run(self):
        self._sock.bind(('', self._port))
        pool = ThreadPoolExecutor(self._max_workers)

        print('[+] Server is running on %s:%s' % (get_local_ip(), self._port))

        try:
            while True:
                resp, addr = self._sock.recvfrom(BUFFER_SIZE)
                pool.submit(self.process_packet, resp, addr)
        except (KeyboardInterrupt):
            self.shutdown()
        finally:
            self._sock.close()

    def process_packet(self, packet, addr):
        pack_type = self.get_packet_type(packet)

        if pack_type == 0:
            self._client_req_handler(addr, packet)
        else:
            raise Exception('Invalid packet')
    
    def get_packet_type(self, packet):
        return packet[3] >> 7