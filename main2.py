import discord
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
from discord.ext.commands.errors import MissingPermissions
from asyncio.tasks import sleep
from treo import keep_alive
client = commands.Bot(command_prefix='..')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def id(ctx, data = ''):
    if data == '':
        await ctx.send(ctx.author.id)
    else:
        await ctx.send(data[3:-1])
    # await ctx.channel.send("<@" + str(us) + ">")

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    if '911980283606204437' in ctx.content :
        await ctx.channel.send('mi tag con bot lam cl gi the??')
    await client.process_commands(ctx)

@client.command()
async def hello(ctx):
    await ctx.channel.send('Hello bn <3')
    await ctx.channel.send('Chuc ban 1 ngay tot lanh')

@client.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.channel.send('Da Vao')
    else:
        await ctx.channel.send('Vo kenh chat trc di')

@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.channel.send('Da thoat')
    else:
        await ctx.channel.send('t out rui kich t lam gi nua;-;')

@client.command()
async def richroll(ctx):
    if ctx.author.voice != None:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.channel.send('Da Vao')
        if not voice.is_playing():
            voice.play(discord.FFmpegPCMAudio("nhac.mp3"), after=None)
            while voice.is_playing():
                await sleep(0.5)
        voice.disconnect()
    else:
        await ctx.channel.send('Vo kenh chat trc di')

@client.command()
async def spam(ctx, data ='', term = ''):
    while(True):
        await ctx.channel.send(data + ' ' + term)

keep_alive()      
client.run('OTExOTgwMjgzNjA2MjA0NDM3.YZpR0w.ox_D6tAxWAjlJgs81_KiQwjGkK4')
