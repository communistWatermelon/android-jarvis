import socket 
import sys

class MessageQueue(object):
	ClientQueue = 0 
	def __init__(self):
		self.terminal = sys.stdout
		self.ClientQueue = client

	def __init__(self, client):
		self.terminal = sys.stdout
		self.ClientQueue = client

	def write(self, message):
		self.ClientQueue.sendall(message)