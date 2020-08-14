
import discord
from discord.ext import commands
import typing
import random
import time
import abc
import rog
import psutil
import matplotlib.pyplot as plt
import asyncio
import youtube_dl
import ffmpeg
from apiclient.discovery import build
import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
import base64
import json
import os
import subprocess
import asyncio
import itertools
import sys
from async_timeout import timeout
from functools import partial
import asyncio
import itertools
import traceback
from youtube_dl.utils import lookup_unit_table
import random
import playlist

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

    
@bot.command()
async def ping(ctx):
    await ctx.send('うi')


bot.run(token)
