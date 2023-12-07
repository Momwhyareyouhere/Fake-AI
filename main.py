import discord
from discord.ext import commands

intents = discord.Intents.all()  # Enable all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ai"))
    print(f"We have logged in as {bot.user}")

bot.run('YOUR_BOT_TOKEN_HERE')  # Replace 'YOUR_BOT_TOKEN_HERE' with your bot's token
