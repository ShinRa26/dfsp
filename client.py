import socket
import threading
import handlers as hdl

def _connect(node_addr):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(node_addr)

    return c

class Client(object):
    def __init__(self, node_addr):
        self.client = _connect(node_addr)


    def send_and_wait(self, msg):
        self.client.send(msg.encode("utf-8"))
        self._parse_msg_tag()


    def _parse_msg_tag(self):
        resp = self.client.recv(1024*1024).decode("utf-8")
        tag, msg = resp[:4], resp[4:]

        if not tag in hdl.CLIENT_TAGS:
            self._close_connection()
            return

        if tag == "UPDT":
            self._close_connection()
            return hdl.CLIENT_TAGS[tag](msg)
        else:
            hdl.CLIENT_TAGS[tag](msg)
            self._close_connection()

    
    def _close_connection(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
