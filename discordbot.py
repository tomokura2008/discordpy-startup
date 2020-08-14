import discord
from discord.ext import commands
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    bot.session = aiohttp.ClientSession(loop=bot.loop)
    while True:

        await bot.change_presence(activity=discord.Game(name="herokuで稼働中"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="更新時間：2020/8/6/21:30"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="ヘルプ表示/help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="目標:"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="discordbot"))
        await asyncio.sleep(15)   

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

     
    
  
    

@bot.command()
async def ping(ctx):
    await ctx.send('うぇーい')


bot.run(token)
