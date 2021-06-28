import discord
import aiohttp
import logparse
import guildparse
import logger
import requests
import os

# Tokens present in token.txt, delimited by comma:
# 0 = Discord
# 1 = FFlogs
try:
	file = open("token.conf", "r")
	token = file.read().split('\n')
	token[0] = token[0].split("=")[1]
	out = open("out/help", "r")
	helpsect = out.read().split("%")
	client = discord.Client()
	server = 0
	# Webhook data
	webhook = open("webhooks.conf", "r").read().split('\n')
	sendHook = -1
	lastMessage = 'NULL'
	logger.clear_old_logs()
except Exception as err:
	logger.set_error_offline("vector.py - globals", str(err))
	exit()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	await client.change_presence(activity=discord.Game(name="Python3"))

async def printoutput(reports, channel):
	for report in reports:
		for out in report:
			if (len(out) > 10):
				await channel.send(out)
				await send_webhook(out)

async def send_webhook(message):
	global lastMessage
	lastMessage = message
	if sendHook > -1 and sendHook < len(webhook):
		data = {
			"content": message
		}
		result = requests.post(webhook[sendHook], json = data)
		result.raise_for_status()

@client.event
async def on_message(message):
	async with aiohttp.ClientSession() as session:
		if message.author == client.user:
			return
		elif 'https://www.fflogs.com/reports/' == message.content[:31]:
			reports = await logparse.get_pulls(message, message.content[31:47], token[1], session)
			for out in reports:
				await message.channel.send(out)
				await send_webhook(out)
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
		elif '.send' == message.content[:5]:
			await send_webhook(lastMessage)
		elif '.github' in message.content:
			await message.channel.send('https://github.com/AleXwern')
		elif '.source' in message.content:
			await message.channel.send('https://github.com/AleXwern/FFXIV-Encounter-Compiler')
		elif '.diary' in message.content:
			await message.channel.send('https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing')
		elif '.rs' in message.content and str(message.author) == 'AleXwern#4074':
			print('Closing connection!')
			await client.close()
		elif '.check' == message.content[:6]:
			await message.channel.send(helpsect[1])
		elif '.hook' == message.content[:5]:
			global sendHook
			sendHook = int(message.content.split(' ')[1])
			await message.channel.send('Webhook status: ' + str(sendHook))


client.run(token[0])
