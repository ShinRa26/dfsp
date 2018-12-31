import os
import pickle
import socket
import threading
import handlers as hdl
from server import Server

PEER_MAX = 128

def make_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# TODO::Split server into own class, getting too busy
class Node(object):
    def __init__(self, max_peers=PEER_MAX):
        self.debug = True
        self.server = Server(max_peers)

        self.server_thread = threading.Thread(
            target=self.server.run_server,
            args=()
        )
        self.server_thread.start()

