import socket
import threading
import handlers as hdl


def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 9000))
    s.listen(1)

    return s


class Server(object):
    def __init__(self, max_peers):
        self.known_peers = []
        self.server = create_server()
        self.is_alive = True


    def run_server(self):
        while self.is_alive:
            connection_thread = threading.Thread(
                target=self._forward_to_handler,
                args=(*self.server.accept(),)
            )
            connection_thread.start()
        
        self._close_connection()


    def _forward_to_handler(self, client, addr):
        msg = client.recv(1024*1024).decode("utf-8")
        tag = msg[:4]

        # If we're getting peers, send the peer list
        if tag == "UPDT":
            self._forward_msg(client, tag, self.known_peers)
        else:
            self._forward_msg(client, tag, msg)

    
    def _forward_msg(self, client, tag, msg):
        if not tag in hdl.SERVER_TAGS.keys():
            self._close_connection(client=client)
            return
        
        hdl.SERVER_TAGS[tag](client, msg)
        self._close_connection(client=client)


    def _close_connection(self, client=None):
        if not client:
            self.server.shutdown(socket.SHUT_RDWR)
            self.server.close()
        else:
            client.shutdown(socket.SHUT_RDWR)
            client.close()

