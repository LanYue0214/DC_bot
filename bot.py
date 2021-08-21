import discord
From discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(">> Bot is online. <<")


bot.run('ODc3NzkxMzIwODM0NDY1Nzky.YR3w3w.w85f8K8rRnw1vyREcMxk72I3T6I')