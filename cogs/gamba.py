import discord
from discord.ext import commands
import random
import sys
import os

class Gamba(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Bot ping is: {round(self.bot.latency,3)*1000} ms')
    
def setup(bot):
    bot.add_cog(Gamba(bot))