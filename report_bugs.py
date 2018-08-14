import discord
import asyncio
import datetime
from discord.ext import commands

cmdPrefix = ';'
client = discord.Client()
botToken = 'duap.DlQukw.i2dNkRKBdPReoqQmA6KJe0ly7xE'

class BugHunter:
	@client.event
	def on_ready(self):
		print('xdddd')

class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', bot.user)
        print('ID:', bot.user.id)

    async def on_message(self, message):
        print(message)

def setup(bot):
    bot.add_cog(Events(bot))

@client.event
def xd():
	print('xdd')
client.run(botToken)
