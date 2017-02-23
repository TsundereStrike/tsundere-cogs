import os
import discord
from discord.ext import commands
import requests

class Smurfy:

    """Discord based Smurfy API Access"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def smurfy(self):
        await self.bot.say("```/pricelist   - Request price list of almost all in-game objects (mechs, items..)```")
        await self.bot.say("```/modulelist  - Request list of modules```")
        await self.bot.say("```/weaponlist  - Request list of weapons```")
        await self.bot.say("```/ammolist    - Request list of ammo```")
        await self.bot.say("```/omnipodlist - Request list of omnipods```")
        await self.bot.say("```/mechlist    - Request list of mechs```")
        await self.bot.say("```/mechbyid    - (work in progress) - Request a specific mech by id```")
        await self.bot.say("```/mechloadout - (work in progress) - Request a mech loadout by ids```")

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
    bot.add_cog(Smurfy(bot))
