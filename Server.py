import socket
import sys
import thread
import os
import subprocess
commands = {}

"""
	Get all the commands from the ini file
"""
def populateCommands():
	with open("commands.ini") as f:
		for line in f:
			(usrCommand, svrCommand) = line.split(":", 1)
			commands[usrCommand] = svrCommand;

"""
	Attempt to process the command. If command doesn't exist, don't blow up.
"""
def processCommand(command):
	try:
		exec commands[command]
	except KeyError:
		print "Command does not exist!"

"""
	Get commands from the client.
"""
def getCommands(client):
	command = ''
	while command != "EXIT":
		command = client.recv(1024)
		processCommand(command, client)
	client.close()

"""
	Start the server, bind the address
"""
def startServer():
	populateCommands()

	PORT = 63555
	HOST = "localhost"

	listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listenSocket.bind((HOST, PORT))
	listenSocket.listen(1)

	while True:
		client, address = listenSocket.accept()
		print 'Connecion Address: ', address
		sys.stdout = client
		thread.start_new_thread(getCommands, (client,))
	listenSocket.close()

startServer()