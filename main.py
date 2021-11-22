import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if ('hello' in message.content):
        await message.channel.send(f'HELLO cc')

client.run('OTExOTgwMjgzNjA2MjA0NDM3.YZpR0w.ox_D6tAxWAjlJgs81_KiQwjGkK4')

