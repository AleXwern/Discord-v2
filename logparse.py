import os
import discord
import requests

logreport = 'https://www.fflogs.com:443/v1/report/fights/'

async def parse_pull(message, code, token):
	if len(code) != 16:
		await message.channel.send('Invalid log!')
		return
	data = requests.get(logreport + code + token)
	if data.status_code != 200:
		await message.channel.send('There\'s an issue on FFlogs side or bad link.')
		return