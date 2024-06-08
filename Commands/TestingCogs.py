import discord
from discord.ext import commands
from discord import app_commands

class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="initial_tests", description="For Testing Purposes")
    async def Testing(self, interaction: discord.Interaction):
        await interaction.response.send_message("Recieved Message")
    
    @app_commands.command(name="latency", description="Retrieve Latency (In Miliseconds [ms])")
    async def Latency(self, interaction: discord.Interaction):
        BotPing = self.bot.latency * 1000
        await interaction.response.send_message(f"Retrieved Bot Ping: {BotPing}ms")
    
    @commands.Cog.listener()
    async def on_message(self, ctx: discord.Message):
        print(ctx.content)

async def setup(bot):
    await bot.add_cog(Testing(bot))