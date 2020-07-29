import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix = "lmgtfy")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
client.run(TOKEN)