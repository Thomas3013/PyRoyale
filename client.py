import socket
import json


class Client:
    def __init__(self, host_ip, hostport):
        self.hostIP = host_ip
        self.hostPort = hostport
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.hostIP, self.hostPort))

    def sendJson(self,data):
        json_data = json.dumps(data)
        self.s.send(json_data.encode('utf-8'))

