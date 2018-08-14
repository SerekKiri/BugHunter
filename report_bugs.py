import discord
import asyncio
import datetime
from discord.ext import commands
from src.config import token

cmdPrefix = ';'
client = discord.Client()
<<<<<<< Updated upstream
=======
botToken = 'NDc4ODY3MTQyNjMzMDYyNDEw.DlQ7Wg.g9CpgSR6r-VZBW4AZovaz_FWU0I'
>>>>>>> Stashed changes

class BugHunter:
    #functions
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