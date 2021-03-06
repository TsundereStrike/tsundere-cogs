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
        url1 = "http://mwo.smurfy-net.de/api/data/prices.json"
        list1 = requests.get(url=url1)
        json1 = list1.json
        await self.bot.say(json1)

    @commands.command()
    async def modulelist(self):
        """Request list of modules"""
        url2 = "http://mwo.smurfy-net.de/api/data/modules.json"
        list2 = requests.get(url=url2)
        json2 = list2.json
        await self.bot.say(json2)

    @commands.command()
    async def weaponlist(self):
        """Request list of weapons"""
        url3 = "http://mwo.smurfy-net.de/api/data/weapons.json"
        list3 = requests.get(url=url3)
        json3 = list3.json
        await self.bot.say(json3)

    @commands.command()
    async def ammolist(self):
        """Request list of ammo"""
        url4 = "http://mwo.smurfy-net.de/api/data/ammo.json"
        list4 = requests.get(url=url4)
        json4 = list4.json
        await self.bot.say(json4)

    @commands.command()
    async def omnipodlist(self):
        """Request list of omnipods"""
        url5 = "http://mwo.smurfy-net.de/api/data/omnipods.json"
        list5 = requests.get(url=url5)
        json5 = list5.json
        await self.bot.say(json5)

    @commands.command()
    async def mechlist(self):
        """Request list of mechs"""
        url6 = "http://mwo.smurfy-net.de/api/data/mechs.json"
        list6 = requests.get(url=url6)
        json6 = list6.json
        await self.bot.say(json6)

    @commands.command()
    async def mechbyid(self):
        """Request a specific mech by id"""
        # todo - 1 needs to be user input id
        url7 = "http://mwo.smurfy-net.de/api/data/mechs/1.json"
        list7 = requests.get(url=url7)
        json7 = list7.json
        await self.bot.say(json7)

    @commands.command()
    async def mechloadout(self):
        """Request a mech loadout by ids"""
        # todo 1
        # 415 needs to be user input mech id
        # todo 2
        # 75a1ea4fcf79e1c24216b1db218a47e6f9888309 needs to be user input loadout id
        url8 = "http://mwo.smurfy-net.de/api/data/mechs/415/loadouts/75a1ea4fcf79e1c24216b1db218a47e6f9888309.json?print=pretty"
        list8 = json.load(urllib2.urlopen(url8))
        json8 = list8.json
        await self.bot.say(json8)
            
def setup(bot):
    bot.add_cog(Smurfy(bot))
