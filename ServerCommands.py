import MessageQueue

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
def processCommand(command, client):
	if command == "EXIT":
		print "Client Disconnecting"
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
		command = client.recv(10)
		command.rstrip()
		processCommand(command, client)
	client.close()
