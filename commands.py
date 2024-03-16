from discord.ext import commands
from discord import FFmpegPCMAudio
from config import config

class Commands(commands.Cog):
    def __init__(self, bot, url):
        self.bot = bot
        self.url = url
    
    @commands.command()
    async def play(self, ctx: commands.Context):
        try:
            voice_channel = ctx.author.voice.channel
            vc = await voice_channel.connect()

            await ctx.send("Playing mad bangers.")
            vc.play(FFmpegPCMAudio(self.url))
        except:
            return await ctx.send("You are not connected to a voice channel.")
        
    @commands.command()
    async def stop(self, ctx: commands.Context):
        try:
            vc = ctx.voice_client
            return await vc.disconnect()
        except:
            return await ctx.send("You are not connected to a voice channel.")

async def setup(bot: commands.Bot):
    URL = config.App().Url
    await bot.add_cog(Commands(bot, URL))
