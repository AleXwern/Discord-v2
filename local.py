import aiohttp
import logparse
import guildparse

file = open("token.txt", "r")
token = file.read().split('\n')
out = open("out/help", "r")
helpsect = out.read().split("%")

async def printoutput(reports, channel):
	for out in reports:
		if (len(out) > 10):
			await print(out)

async def local_parse():
	print('''This is a local and independent way to deal with FFlogs links,\n
			type a command in terminal to execute it or [q] to exit.''')
	async with aiohttp.ClientSession() as session:
		while True:
			command = str(input())
			if 'https://www.fflogs.com/reports/' == command[:31]:
				reports = await logparse.get_pulls([], command[31:47], token[1], session)
				await print(reports)
			elif '.guild' == command[:6]:
				reports = await guildparse.parse_guild(command.split(' '), token[1], [], session)
				await printoutput(reports, [])
			elif '.recrawl' == command[:8]:
				reports = await guildparse.parse_file(token[1], [], session)
				await printoutput(reports, [])
			elif '.user' == command[:5]:
				reports = await guildparse.parse_user(command.split(' '), token[1], [], session)
				await printoutput(reports, [])
			elif '.help' in command:
				await print(helpsect[0])
			elif '.github' in command:
				await print('https://github.com/AleXwern')
			elif '.source' in command:
				await print('https://github.com/AleXwern/FFXIV-Encounter-Compiler')
			elif '.diary' in command:
				await print('https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing')
			elif 'q' in command:
				print('Closing script!')
				break
			elif '.check' == command[:6]:
				await print(helpsect[1])


await local_parse()