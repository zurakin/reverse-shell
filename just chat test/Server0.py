import time
import socket
from connection import Connection
from message import Message


class Server():
    def __init__(self, host, port):
        self.s = socket.socket()
        self.host = host
        self.port = port
        #binding
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        #accepting
        self.conn, self.address = self.s.accept()
        print(f"Connection has been established | IP {self.address[0]} | port {self.address[1]}")
        #communicating with client
        while True:
            #send
            cmd = input('--->')
            self.conn.send(cmd.encode())

            #receive
            ins = self.s.recv(1024) #1024 is buffer size
            # print('here is the ins ', ins)
            # msg = Message(ins ,2)
            # size = msg.size
            # data = msg.utf
            # while len(data) < size:
            #     print('receiving ..............')
            #     data += Message(self.s.recv(1024),1).utf
            # print(data)
            client_response = str(self.conn.recv(10000), "utf-8")
            print(client_response, end = "")
server = Server('192.168.0.103', 1554)
