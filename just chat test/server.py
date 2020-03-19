import socket ,time, sys

class Server():
    def __init__(self):
        self.ip = '192.168.0.103'
        self.port = 1554
        self.s = socket.socket()
        #binding
        self.s.bind((self.ip, self.port))
        print('binding success')
        print('starting listening')
        self.s.listen(5)
        print('done listening')
        self.conn, self.address = self.s.accept()
        print("Connection has been established | IP {} | port {}".format(self.address[0], str(self.address[1])))
        self.communicate()

    def communicate(self):
        while True:
            cmd = input('-->')
            if cmd == 'quit':
                self.conn.send('quit'.encode())
                self.conn.close()
                self.s.close()
                sys.exit()
            elif len(cmd.encode()) > 0:
                self.conn.send(cmd.encode())
                client_response = str(self.conn.recv(10000), "utf-8")
                print(client_response, end = "")

server = Server()
