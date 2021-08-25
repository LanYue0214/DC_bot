#simple command and ping robot is here
from core.classes import Cog_Extension
import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()#how long robot delay
    async def ping(self, ctx): #ctx is a very important agreement ctx = context(上下文), including member id channel id
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)') #round will let number after dot to cut 4 to 5(XDD)
    
    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello')


def setup(bot): #bot = bot = commands.Bot(command_prefix='$',intents = intents) from bot.py
    bot.add_cog(Main(bot))