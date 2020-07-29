import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix = "lmgtf")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def y(ctx, str):
    await ctx.send(f"let me google that for you {str}")

client.run(TOKEN)