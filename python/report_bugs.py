import discord
import asyncio
import datetime
import json
from discord.ext import commands

client = discord.Client()

class BugHunter:
    isReady = False
    cmdPrefix = ''
    botToken = ''
    bugChannel = ''
    bugChannelServerList = []
    lastMsg = 0
    #functions
    async def getChannelByName(self, servername, name):
        logChannel = discord.utils.get(client.get_all_channels(), server__name=servername, name=name)
        return logChannel
    async def loadConfig(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.cmdPrefix = data['prefix']
            self.botToken = data['token']
            self.bugChannel = data['channels']
            server_list = []
            serverlist_file = open ('cfg\\serverlist.json')
            json_array = json.load(input_file)
            channel = discord.utils.get(client.get_all_channels(), server__name='Cool', name='general')
    async def handleCommands(self, command):
        embed=discord.Embed(title="DevStudio", url="https://devstudio.itch.io", color=0x00ff00)
        embed.set_author(name='BugHunter', url='https://github.com/quritto/DenisAskedMeToDoThisBotForReportBugs/tree/master/python', icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ')
        field1name = self.lastMsg.author.nick + ' ' + 'reported bug'
        separatorIndex = command.find(':')
        thumbinail_img = ''
        if(separatorIndex == -1):
            field1value = command[0 : len(command)]
        else:
            field1value = command[0 : command.find(':') - 1]
            thumbinail_img = command[command.find(':') + 1 : len(command)]
        if(thumbinail_img != ''):
            embed.set_thumbnail(url=thumbinail_img)
        embed.add_field(name=field1name, value=field1value, inline=True)
        embed.set_footer(text="BugHunter by R1SK and Kiritito")
        for var in self.bugChannelServerList:
            await var.send(embed=embed)
    #events
    async def onReady(self):
        print('Logged in as', client.user.name, 'with ID', client.user.id)
        print('Loading cfg')
        await self.loadConfig('cfg\\config.json')
        print('Config loaded')
        self.isReady = True
    async def onMessage(self, message):
        if(self.isReady == False):
            return
        if(message.content.startswith('Bugreporter, send messages here')):
            self.bugChannelServerList.append(message.channel)
            print('Channel assigned to', message.channel.name)
            return
        if(message.content.startswith(self.cmdPrefix)):
            self.lastMsg = message
            await self.handleCommands(message.content[len(self.cmdPrefix) : len(message.content)])

mainClass = BugHunter()

@client.event
async def on_ready():
    await mainClass.onReady()
@client.event
async def on_message(message):
    await mainClass.onMessage(message)
#client.run(botToken)
client.run('NDA5Mzk4OTc5NDMzMDcwNTk0.DiqJ4Q.B7rh7f-aeYygaBiscdI3QGo96YY',bot=False,reconnect=True) 