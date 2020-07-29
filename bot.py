import discord
from discord.ext import commands

TOKEN = ""

bot = commands.Bot(command_prefix = "lmgtf")

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@bot.command()
async def y(ctx, str):
    await ctx.send(f"let me google that for you {str}")

bot.run(TOKEN)