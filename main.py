#Jeff Lu & Daniel Sanchez Performance Task 

from http import client
from multiprocessing.connection import Client
import nextcord
from nextcord.ext import commands
import random
import asyncio


intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

# Bot Startup

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=nextcord.Game(name=''))

@bot.event #@bot.event on_'______'(parameters)
async def on_message(message): # on_message (scan for message) (message) (tell bot its a message)
    if message.content == 'bruh' or 'Bruh': #bruh
        await message.channel.send('FUCK') # get channel, send to channel

# Commands

@bot.command()
async def list(ctx):
    await ctx.send('`prefix:.` \n `commands:` \n fuckoff \n nom \n controversy \n photo \n mulsa')


@bot.command()
async def fuckoff(ctx):
    await ctx.send("gay bitch")


@bot.command()
async def cum(ctx):
    await ctx.send(
        "I don't have a penis, I don't  have a dick, I crafted my own, but it just wouldn't stick. I fashioned a phallusto keep for myself -But now it just sitsin a box on a shelf. Oh what I would dofor a wrinkle or a wang! A schlong of my ownto go out with a bang! A gherkin for a jerkin', a pecker, a prick. Won't somebody, somebodyget me a dick")


@bot.command()
async def nom(ctx):
    await ctx.send(file=nextcord.File('bird.png'))


@bot.command()
async def controversy(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(10)
    msg = await ctx.send('bruh')
    await asyncio.sleep(3)
    await msg.delete()


@bot.command()
async def photo(ctx):
    answer = random.randint(1, 40)

    if answer <= 10:
        await ctx.send(file=nextcord.File('bird.png'))
    elif answer <= 20:
        await ctx.send(file=nextcord.File('capture.png'))
    elif answer <= 30:
        await ctx.send(file=nextcord.File('u072qchu43w71.jpg'))
    elif answer <=40:
        await ctx.send(file=nextcord.File('ryjtfuk.png'))
    else:
        await ctx.send(file=nextcord.File('sorry.png'))


@bot.command()
async def mulsa(ctx):
    msg = await ctx.send("wjen")
    await asyncio.sleep(0.5)
    await msg.edit(content="whe")
    await asyncio.sleep(0.5)
    await msg.edit(content="wjehn")
    await asyncio.sleep(0.5)
    await msg.edit(content="whe-")
    await asyncio.sleep(0.1)
    await msg.edit(content="when you")

@bot.command()
async def mrkim(ctx):
    await ctx.send('```___( o)> \n \ <_. ) \n `--- ```')
