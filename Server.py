import socket
import thread
import os

def processCommand(command):
	if command == "MAC":
		print "staring mac"
		os.system('"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm OSX')
	elif command == "KALI":
		print "staring kali"
		os.system('"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm kali')		

def getCommands(client):
	command = ''
	while command != "EXIT":
		print "waiting for data"
		command = client.recv(1024)
		processCommand(command)
	print "exiting"
	client.close()

listenPort 		= 63555
HOST 			= "localhost"

listenSocket 	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.bind((HOST, listenPort))
listenSocket.listen(1)

while True:
	client, address = listenSocket.accept()
	print 'Connecion Address: ', address
	thread.start_new_thread(getCommands, (client,))

listenSocket.close()

