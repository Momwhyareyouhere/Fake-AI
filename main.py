import discord
from discord.ext import commands
from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def roll(ctx):
    import random
    await ctx.send(f'You rolled a {random.randint(1, 6)}.')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def kick(ctx, member: discord.Member):
    owner_role = discord.utils.get(ctx.guild.roles, name="Owner")
    if owner_role in ctx.author.roles:
        await member.kick()
        await ctx.send(f'{member} has been kicked.')
    else:
        await ctx.send("You don't have permission to use this command.")

@bot.command()
async def clear(ctx, amount: int):
    owner_role = discord.utils.get(ctx.guild.roles, name="Owner")
    if owner_role in ctx.author.roles:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("You don't have permission to use this command.")

bot.run('YOUR_BOT_TOKEN')
