import discord
import requests
import logparse
#from math import floor
#from datetime import datetime

url = 'https://www.fflogs.com:443/v1/reports/guild/'

class Guild:
	def __init__(self):
		self.guild = ''
		self.fight = ''
		self.server = ''
		self.region = ''
		self.reports = []

async def parse_guild(arr, token, message):
	guild = Guild()
	if len(arr) < 5 or len(arr) > 5:
		await message.channel.send("Incorrect amount of arguments: " + str(len(arr)) + " instead of 5.\nSee .help for more details.")
	guild.guild = arr[2].replace('_', '%20')
	guild.fight = arr[1].replace('_', ' ').lower()
	guild.server = arr[3]
	guild.region = arr[4]
	data = requests.get(url + guild.guild + '/' + guild.server + '/' + guild.region + '?' + token)
	if data.status_code != 200:
		await message.channel.send('There\'s an issue on FFlogs side or some data was incorrect: ' + str(data.status_code))
		return
	history = data.json()
	for report in history:
		if report['title'].lower() == guild.fight:
			guild.reports.insert(0, report['id'])
	await message.channel.send("Found " + str(len(guild.reports)) + " suitable reports.\nProcessing... (Ultimates take a while to process each)")
	for report in guild.reports:
		print(report)
		await logparse.get_pulls(message, report, token)
	await message.channel.send("All reports processed!")
