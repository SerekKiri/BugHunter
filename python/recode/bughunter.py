import discord
import asyncio
import datetime
import json
import io

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
		self.file = open(self.fileName, 'r')
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
		serverList = []
		for server in self.jsonFile['servers']:
			channelList = []
			for channel in server['channels']:
				channelList.append(channel)
			sServer = CfgServer()
			sServer.initialise(server['name'], channelList)
			serverList.append(sServer)
		return serverList
	def addServer(self, CfgServer):
		file = open(self.fileName, 'r+')
		print(file.read())

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
	#Misc functions
	def isServerAtList(self, serverName):
		for server in self.serverList:
			if(server.name == serverName):
				return True
		return False
	def findAllOccurrences(self, s, ch):
		idxs = []
		for i in range(len(s)):
			if(s[i] == ch):
				idxs.append(i)
		return idxs
	def findCharOffset(self, string, char, offset):
		for x in range(offset, len(string)):
			if(string[x] == char):
				return x
		return -1
	def isCommand(self, message):
		return message.content.startswith(self.cmdPrefix)
	def commandAndArgsFromMessage(self, message):
		hasParams = False
		parameterIndexes = []
		paramCount = 0
		if(message.content.find(self.argSeparator) != -1):
			hasParams = True
		if(self.findCharOffset(message.content, ' ', len(self.cmdPrefix) + 2) != -1):
			hasParams = True
		if(hasParams == False):
			command = message.content[len(self.cmdPrefix) + 1 : len(message.content)]
			return ParsedCommand(command)
		else:
			parameterIndexes = self.findAllOccurrences(message.content, self.argSeparator)
			paramCount = len(parameterIndexes)
			command = message.content[len(self.cmdPrefix) + 1 : self.findCharOffset(message.content, ' ', len(self.cmdPrefix) + 2)]
			args = []
			if(paramCount == 0):
				args.append(message.content[len(self.cmdPrefix) + len(command) + 2 : len(message.content)])
				return ParsedCommand(command, True, args)
			for x in range(0, paramCount + 1):
				if(x == 0):
					args.append(message.content[len(self.cmdPrefix) + len(command) + 2 : parameterIndexes[x]])
					continue
				if(x == paramCount):
					args.append(message.content[parameterIndexes[x - 1] + 2 : len(message.content)])
					continue
				args.append(message.content[parameterIndexes[x - 1] + 2 : parameterIndexes[x] - 1])
			return ParsedCommand(command, True, args)
	def loadConfig(self):
		print('Loading config...')
		config = JConfig('cfg\\config.json')
		data = JConfig('cfg\\data.json')
		config.read()
		data.read()
		self.version = config.readValue('version')
		self.token = config.readValue('token')
		self.cmdPrefix = config.readValue('prefix')
		self.argSeparator = config.readValue('argSeparator')
		self.normalUser = config.readBoolean('normalUser')
		self.serverList = data.readServers()
		newServer = CfgServer()
		data.addServer(newServer)
		print('Config loaded')
	#SubFunctions
	async def sendEmbedAtBotChannelsAtServer(self, server, embed):
		cfgServer = 0
		for x in self.serverList:
			if x.name == server.name:
				cfgServer = x
		for channel in server.channels:
			for channelname in cfgServer.channelList:
				if channel.name == channelname:
					await channel.send(embed=embed)
	def createHelpEmbed(self):
		embed=discord.Embed(title='Help', description='Usage -> bug report bug description (additional -> screenshot)', color=0xff0000)
		embed.set_author(name='BugHunter', url='https://github.com/quritto/DenisAskedMeToDoThisBotForReportBugs', icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ')
		embed.set_footer(text='BugHunter by Kiritito, R1SK and Piter')
		return embed
	def createBugReportEmbed(self, message, parsedMsg):
		title = message.author.name + ' ' + 'sent report'
		embed=discord.Embed(title=title, description=parsedMsg.args[0], color=0xff0000)
		embed.set_author(name='BugHunter', url='https://github.com/quritto/DenisAskedMeToDoThisBotForReportBugs',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ')
		embed.set_footer(text='BugHunter by Kiritito, R1SK and Piter')
		return embed
	#Main functions
	def initialise(self):
		print('BugHunter by R1SK, Kiritito & Piter')
		self.loadConfig()
	#def handleCommands(self, message, parsedMessage):
		#if(parsedMessage.command == 'report'):
			#self.sendEmbedAtMultipleChannels(self.getAllBotChannelsAtServer(message.guild), self.createBugReportEmbed(message, parsedMessage))
		#else:
			#self.sendEmbedAtMultipleChannels(self.getAllBotChannelsAtServer(message.guild), self.createHelpEmbed())
	#Event handlers
	async def onReady(self):
		print('Logged in as', self.client.user.name, 'with ID', self.client.user.id)
		self.isReady = True
	async def onMessage(self, message):
		if(self.isReady == False):
			return
		if(self.isCommand(message) and self.isServerAtList(message.guild.name)):
			msg = self.commandAndArgsFromMessage(message)
			if(msg.command == 'report'):
				await self.sendEmbedAtBotChannelsAtServer(message.guild, self.createBugReportEmbed(message, msg))
			else:
				await self.sendEmbedAtBotChannelsAtServer(message.guild, self.createHelpEmbed())
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