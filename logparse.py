import discord
import requests
from math import floor
import time

logreport = 'https://www.fflogs.com:443/v1/report/fights/'
ulturl = 'https://www.fflogs.com/v1/report/events/casts/'

class TEA:
	lc = bjcc = ts = alex = inc = worm = add = perf = alpha = beta = enrage = 0

class UCoB:
	twin = nael = baha = quick = blck = fell = fall = ten = octet = doub = gold = enrage = 0

class UWU:
	garuda = ifrit = titan = pred = annh = supp = roul = enrage = 0

class Report:
	raidtype = ''
	def __init__(self, zone):
		self.raidtype = zone
	pulls = pullen = maxlen = start = end = raidlen = rpullen = kills = 0

async def alexhandle(url, code, end, tea, teat, token):
	data = requests.get(url)
	if data.status_code != 200:
		return tea
	cast = data.json()
	for c in cast['events']:
		if not (c['ability'] is None):
			if c['ability']['name'] == 'Temporal Interference':
				teat.enrage = 1
			elif c['ability']['name'] == 'Fate Calibration β':
				teat.beta = 1
			elif c['ability']['name'] == 'Fate Calibration α':
				teat.alpha = 1
			elif c['ability']['name'] == 'the Final Word':
				teat.perf = 1
			elif c['ability']['name'] == 'J Wave':
				teat.add = 1
			elif c['ability']['name'] == 'Wormhole Formation':
				teat.worm = 1
			elif c['ability']['name'] == 'Inception Formation':
				teat.inc = 1
			elif c['ability']['name'] == 'Chastening Heat':
				teat.alex = 1
			elif c['ability']['name'] == 'Temporal Stasis':
				teat.ts = 1
			elif c['ability']['name'] == 'J Kick':
				teat.bjcc = 1
			elif c['ability']['name'] == 'Alpha Sword':
				teat.lc = 1
	if not (cast.get('nextPageTimestamp') is None):
		url = ulturl + code + '?start=' + str(cast['nextPageTimestamp']) + '&end=' + str(end) + '&hostility=1&translate=true&' + token
		print(url)
		tea = await alexhandle(url, code, end, tea, teat, token)
	else:
		tea.lc += teat.lc
		tea.bjcc += teat.bjcc
		tea.ts += teat.ts
		tea.alex += teat.alex
		tea.inc += teat.inc
		tea.worm += teat.worm
		tea.add += teat.add
		tea.perf += teat.perf
		tea.alpha += teat.alpha
		tea.beta += teat.beta
		tea.enrage += teat.enrage
	return tea

async def ucobhandle(url, code, end, ucob, ucobt, token):
	data = requests.get(url)
	if data.status_code != 200:
		return ucob
	cast = data.json()
	for c in cast['events']:
		if not (c['ability'] is None):
			if c['ability']['name'] == 'CHECK':
				ucobt.enrage = 1
			elif c['ability']['name'] == 'Morn Afah':
				ucobt.gold = 1
			elif c['ability']['name'] == 'CHECK':
				ucobt.doub = 1
			elif c['ability']['name'] == 'Grand Octet':
				ucobt.octet = 1
			elif c['ability']['name'] == 'Tenstrike Trio':
				ucobt.ten = 1
			elif c['ability']['name'] == 'Heavensfall Trio':
				ucobt.fall = 1
			elif c['ability']['name'] == 'Fellruin Trio':
				ucobt.fell = 1
			elif c['ability']['name'] == 'Blackfire Trio':
				ucobt.blck = 1
			elif c['ability']['name'] == 'Quickmarch Trio':
				ucobt.quick = 1
			elif c['ability']['name'] == 'Seventh Umbral Era':
				ucobt.baha = 1
			elif c['ability']['name'] == 'Heavensfall':
				ucobt.nael = 1
	if not (cast.get('nextPageTimestamp') is None):
		url = ulturl + code + '?start=' + str(cast['nextPageTimestamp']) + '&end=' + str(end) + '&hostility=1&translate=true&' + token
		ucob = await ucobhandle(url, code, end, ucob, ucobt, token)
	else:
		ucob.enrage += ucobt.enrage
		ucob.gold += ucobt.gold
		ucob.doub += ucobt.doub
		ucob.octet += ucobt.octet
		ucob.ten += ucobt.ten
		ucob.fall += ucobt.fall
		ucob.fell += ucobt.fell
		ucob.blck += ucobt.blck
		ucob.quick += ucobt.quick
		ucob.baha += ucobt.baha
		ucob.nael += ucobt.nael
	return ucob

async def uwuhandle(url, code, end, uwu):
	return uwu

async def hhmmss(time):
	hours = floor(time / 3600)
	minutes = floor((time - (hours * 3600)) / 60)
	seconds = time - (hours * 3600) - (minutes * 60)
	if hours < 10:
		hours = "0" + str(hours)
	if minutes < 10:
		minutes = "0" + str(minutes)
	if seconds < 10:
		seconds = "0" + str(seconds)
	return str(hours) + ':' + str(minutes) + ':' + str(seconds)

async def print_logs(encounter, tea, uwu, ucob, message):
	text = ''

	for enc in encounter:
		enc.raidlen = round(enc.raidlen / 1000)
		enc.maxlen = round(enc.maxlen / 1000)
		text = '```*' + enc.raidtype + '*'
		text += '\nTotal pulls:	' + str(enc.pulls)
		#text += '\nStart time:	 ' + enc.startepoch
		#text += '\nEnd time:	   ' + enc.endepoch
		text += '\nTotal kills:	' + str(enc.kills)
		text += '\nRaid length:	' + str(await hhmmss(floor(enc.raidlen)))
		text += '\nMax pull len:   ' + str(await hhmmss(enc.maxlen))
		text += '\nAvg pull len:   ' + str(await hhmmss(floor(enc.raidlen / enc.pulls)))
		if enc.raidtype == 'The Epic of Alexander (Ultimate)':
			text += '\n\nAdditional TEA information - Wipes by phase:'
			text += '\nLL: ' + str(enc.pulls - tea.lc)
			text += ' LC: ' + str(tea.lc - tea.bjcc)
			text += ' BJCC: ' + str(tea.bjcc - tea.ts)
			text += ' TS: ' + str(tea.ts - tea.alex)
			text += ' Alex: ' + str(tea.alex - tea.inc)
			text += ' Inc: ' + str(tea.inc - tea.worm)
			text += ' Worm: ' + str(tea.worm - tea.add)
			text += ' Add: ' + str(tea.add - tea.perf)
			text += ' Perf: ' + str(tea.perf - tea.alpha)
			text += ' Alpha: ' + str(tea.alpha - tea.beta)
			text += ' Beta: ' + str(tea.beta - tea.enrage)
			text += ' Enrage: ' + str(tea.enrage - enc.kills)
			print(str(enc.pulls) + ' ' + str(tea.lc) + ' ' + str(tea.bjcc) + ' ' + str(tea.ts) + ' ' + str(tea.alex) + ' ' + str(tea.inc) + ' ' + str(tea.worm) + ' ' + str(tea.add) + ' ' + str(tea.perf) + ' ' + str(tea.alpha) + ' ' + str(tea.beta) + ' ' + str(tea.enrage))
		elif enc.raidtype == 'the Unending Coil of Bahamut (Ultimate)':
			text += '\n\nAdditional UCoB information - Wipes by phase:'
			text += '\nTwin: ' + str(enc.pulls - ucob.nael)
			text += ' Nael: ' + str(ucob.nael - ucob.baha)
			text += ' Bahamut: ' + str(ucob.baha - ucob.quick)
			text += ' Quick: ' + str(ucob.quick - ucob.blck)
			text += ' Black: ' + str(ucob.blck - ucob.fell)
			text += ' Fell: ' + str(ucob.fell - ucob.fall)
			text += ' Heaven: ' + str(ucob.fall - ucob.ten)
			text += ' Ten: ' + str(ucob.ten - ucob.octet)
			text += ' Octet: ' + str(ucob.octet - ucob.doub)
			text += ' Twin/Nael: ' + str(ucob.doub - ucob.gold)
			text += ' Golden: ' + str(ucob.gold - ucob.enrage)
			text += ' Enrage: ' + str(ucob.enrage - enc.kills)
		elif enc.raidtype == "The Weapon's Refrain (Ultimate)":
			text += '\n\nAdditional UWU information - Wipes by phase:'
			text += '\nGaruda: ' + str(enc.pulls - uwu.ifrit)
			text += ' Ifrit: ' + str(uwu.ifrit - uwu.titan)
			text += ' Titan: ' + str(uwu.titan - uwu.ultima)
			text += ' Ultima: ' + str(uwu.ultima - uwu.enrage)
			text += ' Enrage: ' + str(uwu.enrage - enc.kills)
		text += '```'
		await message.channel.send(text)


async def parse_report(report, code, token, message):
	zone = ''
	enc = []
	tea = TEA()
	ucob = UCoB()
	uwu = UWU()
	i = 0

	for p in report['fights']:
		if zone == '':
			enc.append(Report(p['zoneName']))
			zone = p['zoneName']
		elif p['zoneName'] != zone:
			zone = p['zoneName']
			i += 1
			enc.append(Report(p['zoneName']))
		enc[i].pullen = p['end_time'] - p['start_time']
		if enc[i].pullen > 20000:
			enc[i].pulls += 1
			enc[i].rpullen += enc[i].pullen
		if enc[i].pullen > enc[i].maxlen:
			enc[i].maxlen = enc[i].pullen
		if enc[i].start == 0:
			enc[i].start = p['start_time']
		if p['end_time'] > enc[i].end:
			enc[i].end = p['end_time']
		if not (p.get('kill') is None):
			if p['kill'] == True:
				enc[i].kills += 1
		enc[i].raidlen = enc[i].end - enc[i].start
		if enc[i].pullen > 20000:
			url = ulturl + code + '?start=' + str(p['start_time']) + '&end=' + str(p['end_time']) + '&hostility=1&translate=true&' + token
			if enc[i].raidtype == 'The Epic of Alexander (Ultimate)':
				tea = await alexhandle(url, code, p['end_time'], tea, TEA(), token)
			elif enc[i].raidtype == 'the Unending Coil of Bahamut (Ultimate)':
				ucob = await ucobhandle(url, code, p['end_time'], ucob, UCoB(), token)
			elif enc[i].raidtype == 'The Weapon\'s Refrain (Ultimate)':
				uwu = await uwuhandle(url, code, p['end_time'], uwu)
	await print_logs(enc, tea, uwu, ucob, message)

async def get_pulls(message, code, token):
	if len(code) != 16:
		await message.channel.send('Invalid log!')
		return
	data = requests.get(logreport + code + '?' + token)
	if data.status_code != 200:
		await message.channel.send('There\'s an issue on FFlogs side or bad link.')
		return
	await parse_report(data.json(), code, token, message)
		