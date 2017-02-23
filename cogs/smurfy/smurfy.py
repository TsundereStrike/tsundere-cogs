import discord
from discord.ext import commands
import requests

# You must enter your api key here, to generate a new key visit: http:/mwo.smurfy-net.de/change-password
# Once registered and authenticated visiting that URL will allow you to generate a new api key
smurfy_access_token = ''

class Smurfy:

    """Discord based Smurfy API Access"""
    
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/smurfy/credentials.json"
        self.credentials = dataIO.load_json(self.file_path)

    @commands.command(pass_context=True)
    async def smurfyset(self, ctx):
        """Sets your Smurfy API key that you generated from the website: http:/mwo.smurfy-net.de/change-password"""
        await self.bot.whisper("Type your api key. You can reply in this private msg")
        access_token = await self.bot.wait_for_message(timeout=15, author=ctx.message.author)
        if access_token is None:
            return
        else:
            self.credentials["apiKey"] = access_token.content
            dataIO.save_json(self.file_path, self.credentials)
            await self.bot.whisper("Setup complete. API key added. Type /help smurfy to learn more.")

    @commands.command()
    async def pricelist(self):
        """Request price list of almost all in-game objects (mechs, items..)"""
        url1 = "http:/mwo.smurfy-net.de/api/data/prices.json?print=pretty"
        list1 = requests.get(url=url1)
        await self.bot.say(list1)

    @commands.command()
    async def modulelist(self):
        """Request list of modules"""
        url2 = "http://mwo.smurfy-net.de/api/data/modules.json?print=pretty"
        list2 = requests.get(url=url2)
        await self.bot.say(list2)

    @commands.command()
    async def weaponlist(self):
        """Request list of weapons"""
        url3 = "http://mwo.smurfy-net.de/api/data/weapons.json?print=pretty"
        list3 = requests.get(url=url3)
        await self.bot.say(list3)

    @commands.command()
    async def ammolist(self):
        """Request list of ammo"""
        url4 = "http://mwo.smurfy-net.de/api/data/ammo.json?print=pretty"
        list4 = requests.get(url=url4)
        await self.bot.say(list4)

    @commands.command()
    async def omnipodlist(self):
        """Request list of omnipods"""
        url5 = "http://mwo.smurfy-net.de/api/data/omnipods.json?print=pretty"
        list5 = requests.get(url=url5)
        await self.bot.say(list5)

    @commands.command()
    async def mechlist(self):
        """Request list of mechs"""
        url6 = "http:/mwo.smurfy-net.de/api/data/mechs.json?print=pretty"
        list6 = requests.get(url=url6)
        await self.bot.say(list6)

    @commands.command()
    async def mechbyid(self):
        """Request a specific mech by id"""
        # todo - 1 needs to be user input id
        url7 = "http:/mwo.smurfy-net.de/api/data/mechs/1.json?print=pretty"
        list7 = requests.get(url=url7)
        await self.bot.say(list7)

    @commands.command()
    async def mechloadout(self):
        """Request a mech loadout by ids"""
        # todo 1
        # 415 needs to be user input mech id
        # todo 2
        # 75a1ea4fcf79e1c24216b1db218a47e6f9888309 needs to be user input loadout id
        url8 = "http:/mwo.smurfy-net.de/api/data/mechs/415/loadouts/75a1ea4fcf79e1c24216b1db218a47e6f9888309.json?print=pretty"
        list8 = json.load(urllib2.urlopen(url8))
        await self.bot.say(list8)
            

def setup(bot):
    bot.add_cog(Mwo(bot))
