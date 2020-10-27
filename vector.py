import discord
import aiohttp
import logparse
import guildparse

# Tokens present in token.txt, delimited by comma:
# 0 = Discord
# 1 = FFlogs
file = open("token.txt", "r")
token = file.read().split(',')
out = open("out/help", "r")
helpsect = out.read().split("Â")
client = discord.Client()
server = 0

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	await client.change_presence(activity=discord.Game(name="Python3.6.3"))

async def printoutput(reports, channel):
	for out in reports:
		if (len(out) > 10):
			await channel.send(out)

@client.event
async def on_message(message):
	async with aiohttp.ClientSession() as session:
		if message.author == client.user:
			return
		elif 'https://www.fflogs.com/reports/' == message.content[:31]:
			report = await logparse.get_pulls(message, message.content[31:47], token[1], session)
			await message.channel.send(report)
		elif '.guild' == message.content[:6]:
			reports = await guildparse.parse_guild(message.content.split(' '), token[1], message, session)
			await printoutput(reports, message.channel)
		elif '.recrawl' == message.content[:8]:
			reports = await guildparse.parse_file(token[1], message, session)
			await printoutput(reports, message.channel)
		elif '.user' == message.content[:5]:
			reports = await guildparse.parse_user(message.content.split(' '), token[1], message, session)
			await printoutput(reports, message.channel)
		elif '.help' in message.content:
			await message.channel.send(helpsect[0])
		elif '.github' in message.content:
			await message.channel.send('https://github.com/AleXwern')
		elif '.source' in message.content:
			await message.channel.send('https://github.com/AleXwern/FFXIV-Encounter-Compiler')
		elif '.diary' in message.content:
			await message.channel.send('https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing')
		elif '.rs' in message.content and str(message.author) == 'AleXwern#4074':
			print('Closing connection!')
			await client.close()

client.run(token[0])
