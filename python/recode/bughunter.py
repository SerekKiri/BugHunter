import discord
import asyncio
import datetime
import json

#Structure for single server
class CfgServer:
	name = ''
	channelList = []
	def initialise(self, serverName, channels):
		self.name = serverName
		self.channelList = channels

#Structure for handling commands
class ParsedCommand:
	command = ''
	args = []
	hasArgs = False
	argCount = 0
	def __init__(self, Cmd, HasArgs = False, Args = []):
		self.command = Cmd
		self.hasArgs = HasArgs
		if(self.hasArgs):
			self.args = Args
			self.argCount = len(self.args)

#Simple config class
class JConfig:
	fileName = ''
	jsonFile = 0
	def __init__(self, cfgName):
		self.fileName = cfgName
	def read(self):
		self.file = open(self.fileName, 'r+')
		self.jsonFile = json.load(self.file)
		self.file.close()
	def readValue(self, name):
		return self.jsonFile[name]
	def readBoolean(self, name):
		value = self.readValue(name)
		if(value == 'false'):
			return False
		return True
	def readServers(self):
		print(self.jsonFile)
		serverList = []
		for server in self.jsonFile['servers']:
			channelList = []
			for channel in server['channels']:
				channelList.append(channel)
			sServer = CfgServer()
			sServer.initialise(server['name'], channelList)
			serverList.append(sServer)
		return serverList

#Main class
class BugHunter:
	#Variables
	isReady = False
	serverList = []
	version = 0
	name = 'BugHunter'
	token = ''
	normalUser = False
	cmdPrefix = ''
	argSeparator = ''
	client = discord.Client()
	#SubFunctions

	#Misc functions
	def findAllOccurrences(s, ch):
		return [i for i, letter in enumerate(s) if letter == ch]
	def isCommand(self, message):
		return message.content.startswith(self.cmdPrefix)
	def commandAndArgsFromMessage(self, message):
		hasParams = False
		parameterIndexes = []
		paramCount = 0
		if(message.content.find(argSeparator)):
			hasParams = True
		if(hasParams == False):
			command = message.content[len(self.cmdPrefix) : len(message.content)]
			return ParsedCommand(command)
		else:
			parameterIndexes = findAllOccurrences(message.content, argSeparator)
			paramCount = len(parameterIndexes)
			command = message.content[len(self.cmdPrefix) : parameterIndexes[0]]
			args = []
			for x in range(0, argCount):
				args.append(message.content[parameterIndexes[x - 1] : parameterIndexes[x]])
			return ParsedCommand(command, command, True, args)
	def loadConfig(self):
		print('Loading config...')
		config = JConfig('cfg\\config.json')
		data = JConfig('cfg\\data.json')
		config.read()
		self.version = config.readValue('version')
		self.token = config.readValue('token')
		self.cmdPrefix = config.readValue('prefix')
		self.argSeparator = config.readValue('argSeparator')
		self.normalUser = config.readBoolean('normalUser')
		self.serverList = data.readServers()
		print('\nqffwqfwq\n\nfwq\n\nqwffwqfwqfwq')
		print(self.version, self.token, self.cmdPrefix, self.argSeparator. self.normalUser, self.serverList)
		print('\nfwqfwqfwq\nfwqfwq\n')
		print('Config loaded')
	#Main functions
	def initialise(self):
		self.loadConfig()
	#Event handlers
	async def onReady(self):
		print('BugHunter by R1SK & Kiritito')
		print('Logged in as', client.user.name, 'with ID', client.user.id)
		isReady = True
	async def onMessage(self, message):
		if(self.isReady == False):
			return
		if(self.isCommand(message)):
			msg = commandAndArgsFromMessage(message)
			print(msg.command, msg.args, msg.hasArgs, msg.argCount)

Main = BugHunter() 

Main.initialise()

@Main.client.event
async def on_ready():
	await Main.onReady()
@Main.client.event
async def on_message(message):
	await Main.onMessage(message)
if(Main.normalUser):
	Main.client.run(Main.token, bot=False, reconnect=True)
else:
	Main.client.run(Main.token)