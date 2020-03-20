import Server, sys, _thread

def main():
    server = Server.Server('192.168.1.11', 1554)
    while True:
        cmd = input('-->')
        if cmd == 'list clients':
            server.list_clients()
        elif cmd == 'accept':
            acc = _thread.start_new_thread(server.accept, ())
        elif cmd.split(' ')[0] == 'connect':
            i = int(cmd.split(' ')[1])
            print(f'Connected to client {str(i)}')
            server.communicate(i)
            print(f'connection closed with client {i}')
        elif cmd == 'exit':
            sys.exit()

if __name__ == "__main__":
    main()
