# Libraries
import discord, os, asyncio
from dotenv import load_dotenv
from discord.ext import commands

# Load in the Discord Token
load_dotenv("credentials.env")
Discord_Token = os.getenv('DISCORD_BOT_TOKEN')

# Bot
Bot = commands.Bot(command_prefix="!", help_command=None, case_insensitive=True, intents=discord.Intents.all())

async def load_cog():
    for filename in os.listdir('./Commands'):
        if filename.endswith('.py'):
            Bot.load_extension(f'Commands.{filename[:-3]}')

asyncio.run(load_cog())

@Bot.event
async def on_ready():
    await Bot.tree.sync()

Bot.run(Discord_Token)