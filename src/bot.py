import discord
from discord.ext import commands
import random

TOKEN = ""

bot = commands.Bot(command_prefix = "lmgtf")

phrases = ["Let Me Google That For You", "Contrary to popular belief, there are stupid questions. Here's the answer to yours:", "You could have done this yourself, but here you go:", "You should know this by now", "The answer is so obvious", "You clearly aren't very good at this game"]

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def y(ctx, str):
    link = f"https://lmgtfy.com/?q={str.replace(' ', '+')}"
    seed = random.randrange(0, len(phrases))
    phrase = phrases[seed]

    await ctx.send(f"`{phrase}`\n{link}")

bot.run(TOKEN)
