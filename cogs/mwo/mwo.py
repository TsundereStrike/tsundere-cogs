import discord
from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup

class Mwo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mwolist(self):
        """Checks number of players currently playing through steam"""
        url1 = "https://steamdb.info/app/342200/graphs/"
        async with aiohttp.get(url1) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:
                online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
                await self.bot.say(online + ' players are playing MechWarrior Online™ using Steam at this exact moment.')
            except:
                await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

    @commands.command()
    async def mwoserver(self):
        """Checks if MWO server is up"""
        url2 = "https://mwomercs.com/status"
        async with aiohttp.get(url2) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:
                serverStatus = soupObject.find("div", {"id": "statusTextInner"}).get_text()
                await self.bot.say('MechWarrior Online™ Server Status: ' + serverStatus)
            except:
                await self.bot.say("Couldn't load server status.")

    @commands.command()
    async def mwotournament(self):
        """Grabs current MWO information"""
        url3 = "https://mwomercs.com/tournaments"
        async with aiohttp.get(url3) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:
                tournamentName = soupObject.find(class_='eventSelector').find('h2').get_text()
                await self.bot.say('MechWarrior Online™ Current Tournament: ' + tournamentName)
            except:
                await self.bot.say("Couldn't load server status.")
            

def setup(bot):
    bot.add_cog(Mwo(bot))
