import discord
from discord.ext import commands

TOKEN = ""

client = discord.Client(command_prefix = "lmgtfy")

@client.event
async def on_ready():
    print('Bot is ready.')
    
client.run(TOKEN)