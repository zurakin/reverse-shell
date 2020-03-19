import time
import socket
from connection import Connection
from message import Message


class Server():
    def __init__(self, host, port):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = host
            self.port = port
            self.clients = []
        except :
            print('Socket creation failed')

        self.bind()
        self.accept()

    def bind(self):
        try:
            self.s.bind((self.host, self.port))
            self.s.listen(5)
        except socket.error as msg:
            print("Socket binding error: " + str(msg)+ "\n"+ "Retrying...")
            time.sleep(1)
            self.bind()

    def accept(self):
        conn, address = self.s.accept()
        self.clients.append(Connection(conn, address))
        print(f"Connection has been established | IP {address[0]} | port {address[1]}")

    def send_msg(self, connection_id):
        conn = self.clients[connection_id].conn
        cmd = Message(input(), 0)
        if cmd.utf == 'quit':
            conn.send(Message('quit').message)
            conn.close()
            print('connection closed')
            self.clients.pop(connection_id)
            return False
        elif len(cmd.utf) > 0:
            conn.send(cmd.message)
            client_response = self.receive(connection_id)
            print('Client:\n'+ client_response, end = "")

    def communicate(self, connection_id):
        while True:
            a = self.send_msg(connection_id)
            if a == False:
                break
    def receive(self, connection_id):
        conn = self.clients[connection_id].conn
        msg = Message(conn.recv(16) ,2) #1024 is buffer size
        size = msg.get_size()
        data = msg.utf
        while len(data) < size:
            data += Message(conn.recv(16),1).utf
        return data

    def list_clients(self):
        for i, c in enumerate(self.clients):
            print(f'{i} | IP: {c.address[0]} | Port : {c.address[1]}')
