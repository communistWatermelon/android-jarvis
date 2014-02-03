import socket
import sys
import thread
import os
import subprocess
import ServerCommands

"""
	Start the server, bind the address
"""
def startServer():
	ServerCommands.populateCommands()

	PORT = 63555
	HOST = "localhost"

	listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listenSocket.bind((HOST, PORT))
	listenSocket.listen(1)

	while True:
		client, address = listenSocket.accept()
		print 'Connecion Address: ', address
		#sys.stdout = client
		thread.start_new_thread(ServerCommands.getCommands, (client,))
	listenSocket.close()

startServer()