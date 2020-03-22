# reverse-shell
A way to remotely control a computer.

For now, both machines (server and client) must be running python 3. A .exe version will be available when the project is finished.

# How to use:
First, edit both start_client.py and start_server.py and set the host as the ip address of the server. To get the ip address of the server, start a Command Prompt (search for 'cmd' in the windows search bar ) and type 'ipconfig'. This will show you your ip address as IPv4 Address. If the server and the client aren't connected to the same network, the IP will be the server's public IP.

Run start_server.py on you server's machine (the machine that controls the clients).

Run start_client.py no the client's machine.

Now we're done with the client machine.

In the server machine type 'accept' to start accepting connections.

Once a client connects you will see it's information (Id, Ip, port).

You can list your clients by typing 'list clients'.

To connect to a client type 'connect ' followed by the id of the client. ex:'connect 0'.

Once you are connected to a client, you get full access of it. Any command you type will be executed on the client's machine and you will get it's output.

In addition to shell commands you can use a command from additional commands to execute more complex processes.


# Basic shell commands (cheat sheet for newbies):
shutdown -s -t 10: turn off the client's computer in 10 seconds.

dir : display the content of the current working directory.

start spotify.exe : run spotify.exe on the client's machine.

start http://www.facebook.com : start facebook on the client's browser.

echo 'blablabla' > "test.txt" : create a file named test.txt with the content 'blablabla' in the current working directory.

rmdir "test" : remove the folder test.

mkdir "test" : make a new folder test.

del "test.txt" : delete the file test.txt.

copy test.txt "new folder\test.txt" : this one is self-explanatory, seek help if you don't understand.

cut test.txt "new folder\test.txt"  : this one is self-explanatory, seek help if you don't understand.

ping google.com : ping the server google.com and return the output.

# Additional commands:
cd 'directory' : change the current working directory

alert 'message' : display a message on the client's machine.

download 'file_location' : download file from the client's machine.

upload 'file_location' : upload file to the client's machine on the current working directory.

quit : disconnect from the current client. 

back : go back to the first menu to connecto to other clients without disconnecting from the current client. 
