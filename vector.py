import discord
import requests
import logparse
import guildparse

# Tokens present in token.txt, delimited by comma:
# 0 = Discord
# 1 = FFlogs
file = open("token.txt", "r")
token = file.read().split(',')
out = open("out/help", "r")
client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	await client.change_presence(activity=discord.Game(name="Python3.6.3"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif 'https://www.fflogs.com/reports/' == message.content[:31]:
		await logparse.get_pulls(message, message.content[31:47], token[1])
	elif '.guild' == message.content[:6]:
		await guildparse.parse_guild(message.content.split(' '), token[1], message)
	elif '.help' in message.content:
		await message.channel.send(out.read().split("Â")[0])
	elif '.github' in message.content:
		await message.channel.send('https://github.com/AleXwern')
	elif '.source' in message.content:
		await message.channel.send('https://github.com/AleXwern/Discord-v2')
	elif '.diary' in message.content:
		await message.channel.send('https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing')
	elif '.rs' in message.content and str(message.author) == 'AleXwern#4074':
		print('Closing connection!')
		await client.close()
	else:
		print(str(message.author) + ' sent: ' + message.content)

client.run(token[0])