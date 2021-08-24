#put all classes which i may use in futurn
import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        