import dropbox
import discord
from discord.ext import commands

# Add OAuth2 access token here. 
# You can generate one for yourself in the App Console.
# See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
app_key = ''
app_secret = ''
access_token = ''

class Upload:
    """Uploading stuff"""

    def __init__(self, bot, access_token):
        self.bot = bot
        self.access_token = access_token

    @commands.command()
    async def upload(self, ctx, user : discord.Member=None):
        """Uploading stuff for user"""
        img = ctx.rsplit('/', 1)[-1]
        imgName = '/' + img
        await self.bot.say("image to upload: " + imgName)
        await self.bot.say("Testing started...")
        await self.bot.say("url user submitted: " + ctx)
        await self.bot.say("user that initiated command: " + user.name)
        client = dropbox.client.DropboxClient(TOKEN)
        await self.bot.say('linked account: ', client.account_info())
        imgUrl = ctx 
        response = client.put_file(imgName,imgUrl)
        await self.bot.say('uploaded: ', response)
        folder_metadata = client.metadata('/')
        await self.bot.say('metadata: ', folder_metadata)
        f, metadata = client.get_file_and_metadata(imgName)
        out = open(imgName, 'wb')
        out.write(ctx.read())
        out.close()
        await self.bot.say('metadata: ' + metadata)
        await self.bot.say(user.mention + "Your image has been uploaded to the Grog Corps dropbox here: http://tiny.cc/grogcorps")

def setup(bot):
    bot.add_cog(Upload(bot))
