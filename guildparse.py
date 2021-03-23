import discord
import aiohttp
import logparse
import asyncio

url = 'https://www.fflogs.com:443/v1/reports/guild/'
url2 = 'https://www.fflogs.com:443/v1/reports/user/'

class Guild:
	def __init__(self):
		self.guild = ''
		self.fight = ''
		self.server = ''
		self.region = ''
		self.reports = []

async def comp_fights(guild, token, message, data, session):
	if data.status != 200:
		await message.channel.send('There\'s an issue on FFlogs side or some data was incorrect: ' + str(data.status))
		return ([])
	history = await data.json()
	for report in history:
		if report['title'].lower() == guild.fight:
			guild.reports.insert(0, report['id'])
	await message.channel.send("Found " + str(len(guild.reports)) + " suitable reports.\nProcessing... (Ultimates take a while to process each)")
	ret = await asyncio.gather(*[logparse.get_pulls(message, guild.reports[i], token, session) for i in range(len(guild.reports))])
	await message.channel.send("All reports processed!")
	return (ret)

async def parse_guild(arr, token, message, session):
	guild = Guild()
	if len(arr) < 5 or len(arr) > 5:
		await message.channel.send("Incorrect amount of arguments: " + str(len(arr)) + " instead of 5.\nSee .help for more details.")
		return ([])
	guild.guild = arr[2].replace('_', '%20')
	guild.fight = arr[1].replace('_', ' ').lower()
	guild.server = arr[3]
	guild.region = arr[4]
	async with session.get(url + guild.guild + '/' + guild.server + '/' + guild.region + '?' + token) as data:
		return (await comp_fights(guild, token, message, data, session))

async def parse_user(arr, token, message, session):
	guild = Guild()
	if len(arr) < 3 or len(arr) > 3:
		await message.channel.send("Missing user or too much garbage data.\nSee .help for more details.")
		return ([])
	guild.guild = arr[2].replace('_', '%20')
	guild.fight = arr[1].replace('_', ' ').lower()
	async with session.get(url2 + guild.guild + '?' + token) as data:
		return (await comp_fights(guild, token, message, data, session))

async def parse_file(token, message, session):
	file = open("logarr.txt", "r")
	reports = file.read().split('\n')
	ret = await asyncio.gather(*[logparse.get_pulls(message, reports[i][31:47], token, session) for i in range(len(reports))])
	await message.channel.send('All logs processed!')
	return (ret)
