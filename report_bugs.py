import discord
import asyncio
import datetime
import json
from discord.ext import commands

cmdPrefix = ''
client = discord.Client()
botToken = ''

class BugHunter:
    #functions
    async def loadConfig(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            cmdPrefix = data['prefix']
            botToken = data['token']
    async def handleCommands(self, command):
        
    #events
    async def onReady(self):
        print('Logged in as', client.user.name, 'with ID', client.user.id)
    async def onMessage(self, message):
        

mainClass = BugHunter()

@client.event
async def on_ready():
    await mainClass.onReady()
@client.event
async def on_message(message):
    mainClass.onMessage(message)
client.run(botToken)