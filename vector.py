import os
import discord
import requests
import logparse
from multiprocessing import Process

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
		await logparse.parse_pull(message, message.content[31:47], token[1])
	elif '.help' in message.content:
		await message.channel.send(out.read().split("Â")[0])
	elif '.github' in message.content:
		await message.channel.send('https://github.com/AleXwern')
	elif '.rs' in message.content and str(message.author) == 'AleXwern#4074':
		print('Closing connection!')
		await client.close()
	else:
		print(str(message.author) + ' sent: ' + str(message.content))

client.run(token[0])