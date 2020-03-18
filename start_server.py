import Server

def main():
    server = Server.Server('192.168.1.11', 1554)
    while True:
        cmd = input('-->')
        if cmd == 'list clients':
            server.list_clients()
        elif cmd.split(' ')[0] == 'connect':
            i = int(cmd.split(' ')[1])
            print(f'Connected to client {str(i)}')
            server.communicate(i)
            print(f'connection closed with client {i}')

if __name__ == "__main__":
    main()
