import discord
form discord import commands
import random
import sys
import os

class Basic(commands.Cog):
    def __init__(self,bot):
        sellf.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong')

def setup(bot):
    bot.add_cog(Basic(bot))