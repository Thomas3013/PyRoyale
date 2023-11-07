import socket
import json


class Server:
    def __init__(self, hostip, hostport):
        self.hostIP = hostip
        self.port = hostport
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.hostIP, self.port))
        self.s.listen(5)

    def start(self):
        print("Server listening on", self.hostIP, "port", self.port)
        clientsocket, address = self.s.accept()
        print("Connection from", address)
        received_data = clientsocket.recv(1024).decode("utf-8")
        if received_data is not None:
            return json.loads(received_data)

    def close(self, clientsocket):
        clientsocket.close()
        self.s.close()
