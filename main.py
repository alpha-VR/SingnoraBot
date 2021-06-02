import discord
from discord.ext import commands
import os
import sys
import random
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN == None:
    with open('./BOT_TOKEN.token','r') as token:
        BOT_TOKEN = token.read()

bot = commands.Bot(command_prefix = "$")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(BOT_TOKEN)
