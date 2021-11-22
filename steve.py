import discord
client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if('hello'in message.content):
        await message.channel.send('lô cc')
    if('d'in message.content):
        await message.channel.send('tháng nnn hentai ít thôi')
    if('v'in message.content):
        await message.channel.send('tháng nnn hentai ít thôi')
  

client.run('OTEyMTUyMTgxNTM5NTA0MTQ5.YZrx6w.rHmimP61pDR3euU_6xtRjv5x6bE')