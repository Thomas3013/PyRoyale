import socket
import json

class Server:
    def __init__(self,hostip):
        self.hostIP = hostip
        self.port = 1234
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.hostIP,self.port))

    def start(self):
        self.s.listen(5)
        print("Server listening on", self.hostIP, "port", self.port)
        clientsocket, address = self.s.accept()
        print("Connection from", address)
        received_data = clientsocket.recv(1024).decode("utf-8")
        clientsocket.close()
        self.s.close()
        return json.loads(received_data)


