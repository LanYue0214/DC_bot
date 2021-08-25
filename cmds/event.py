#i put event in here
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json',mode = 'r', encoding='utf8') as jfile: #r is read
    jdata = json.load(jfile)
    jfile.close()


class Event(Cog_Extension):

    @commands.Cog.listener() #if anyone join the DC
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        
        with open('setting.json',mode = 'r', encoding='utf8') as jfile: #r is read
            jdata = json.load(jfile)
            jfile.close()
            
        for key in jdata['ban']:
            if key in msg.content:
                await msg.delete()
                await msg.channel.send('{.author}!'.format(msg)+' 你說的話被Ban了。')

        #如果以「說」開頭
        if msg.content.startswith('說'):
            #分割訊息成兩份
            tmp = msg.content.split(" ",2)
            #如果分割後串列長度只有1
            if len(tmp) == 1:
                await msg.channel.send('{.author}!'.format(msg)+" 你要我說什麼啦？")
            #下面四行沒反應，晚點弄
            else:
                counter = False
                for key in jdata['bad_words']:
                    if key in tmp:
                        await msg.channel.send('{.author}!'.format(msg)+' 請不要說髒話!愛莉絲要生氣囉!')
                        counter = True
                        return 
                if counter==False:
                    await msg.channel.send(tmp[1])
            #到這行之前

        if msg.content.startswith('跟我打聲招呼吧'):
            channel = msg.channel
            #機器人叫你先跟他說你好
            await channel.send('那你先跟我說你好')
		        #檢查函式，確認使用者是否在相同頻道打上「你好」
            def checkmessage(m):
                return m.content == '你好' and m.channel == channel
	            #獲取傳訊息的資訊(message是類型，也可以用reaction_add等等動作)
            msg = await self.bot.wait_for('message', check=checkmessage)
            await channel.send('嗨, {.author}!'.format(msg))

        for key in jdata['no_liar']:#msg.content.startswith('我好帥'): #
            if key in msg.content: 
                #刪除傳送者的訊息
                await msg.delete()
                #然後回傳訊息
                await msg.channel.send('不要騙人啦，騙人是不好的行為，愛莉絲嚴肅的說。') 

        for key in jdata['bad_words']:
            if key in msg.content:
                await msg.channel.send('{.author}!'.format(msg)+' 請不要說髒話!愛莉絲要生氣囉!')
                return
                
        #if msg.content.startswith('不要學他們說'):
        #if msg.content.startswith('愛莉絲'):


def setup(bot): 
    bot.add_cog(Event(bot))