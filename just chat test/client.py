import socket, sys

class Client():
    def __init__(self):
        self.ip = '192.168.0.103'
        self.port = 1554
        self.s = socket.socket()
        self.s.connect((self.ip, self.port))
        self.communicate()
    def communicate(self):
        while True:
            data = self.s.recv(1024) #1024 is buffer size
            str_data = data.decode("utf-8")
            if str_data == 'quit':
                self.s.close()
                sys.exit()
            print(str_data)
            self.s.send(input('--->').encode())

client = Client()
