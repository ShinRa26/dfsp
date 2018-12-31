import threading
import handlers as hdl
from server import Server

PEER_MAX = 128

class Node(object):
    def __init__(self, max_peers=PEER_MAX):
        self.debug = True
        self.server = Server(max_peers)

        self.server_thread = threading.Thread(
            target=self.server.run_server,
            args=()
        )
        self.server_thread.start()


    def __del__(self):
        self.server.is_alive = False
        self.server_thread.join()