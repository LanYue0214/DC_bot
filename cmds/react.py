#Reaction OWO
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode = 'r', encoding='utf8') as jfile: #r is read
    jdata = json.load(jfile)
    jfile.close()

class React(Cog_Extension):

    @commands.command()
    async def 圖片(self, ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file = pic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def new(self, ctx, key, arg2):
        if key in jdata:
            if arg2 in jdata[key]: #rewrite not get the data
                await ctx.send( arg2 + ' had been in data.')
            else:
                jdata[key].append(arg2) #rewrite put data in json
                await ctx.send(arg2 + ' is added.')
                with open('setting.json',mode = 'w') as jfile: #w is write
                    json.dump(jdata, jfile, sort_keys = True, indent=4) #using wjdata to store the new data
                    jfile.close()
        else:
            await ctx.send('No ' + key + ' this keyword.')


def setup(bot): #bot = bot = commands.Bot(command_prefix='$',intents = intents) from bot.py
    bot.add_cog(React(bot))