import socket
import threading

HOST = 'localhost'
PORT = 63555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

command = "1"

while command != "EXIT":
	command = raw_input()
	command.rstrip('\r\n')
	s.sendall(command)
	data = s.recv(1024)
	print data
