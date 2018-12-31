import socket
import threading

def _connect(node_addr):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(node_addr)

    return c

class Client(object):
    def __init__(self, node_addr):
        self.client = _connect(node_addr)

    def parse(self):
        pass
