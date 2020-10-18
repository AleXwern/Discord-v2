import discord
import requests
from math import floor
from datetime import datetime

logreport = 'https://www.fflogs.com:443/v1/report/fights/'
ulturl = 'https://www.fflogs.com/v1/report/events/casts/'
dformat = "%a %d %b %Y at %H:%M:%S"

class TEA:
	def __init__(self, enrage):
		self.lc = self.bjcc = self.ts = self.alex = self.inc = self.worm = self.add = self.perf = self.alpha = self.beta = 0
		self.enrage = 0
		if enrage == True:
			self.enrage = 1

class UCoB:
	def __init__(self, enrage):
		self.twin = self.nael = self.baha = self.quick = self.blck = self.fell = self.fall = self.ten = self.octet = self.doub = self.gold = 0
		self.enrage = 0
		if enrage == True:
			self.enrage = 1

class UWU:
	def __init__(self, enrage):
		self.garuda = self.ifrit = self.titan = self.inter = self.ultima = self.pred = self.annh = self.supp = self.roul = 0
		self.enrage = 0
		if enrage == True:
			self.enrage = 1

class Report:
	raidtype = ''
	def __init__(self, zone):
		self.raidtype = zone
		self.tea = TEA(False)
		self.ucob = UCoB(False)
		self.uwu = UWU(False)
		self.pulls = self.pullen = self.maxlen = self.start = self.end = self.raidlen = self.rpullen = self.kills = 0
		self.fightid = [0, 0]

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
			#print(c['ability']['name'])
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
			if c['ability']['name'] == 'Attack':
				continue
			elif c['ability']['name'] == 'Liquid Hell':
				continue
			if c['ability']['name'] == 'Morn Afah':
				ucobt.gold += 1
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
			#print(c['ability']['name'])
	if not (cast.get('nextPageTimestamp') is None):
		url = ulturl + code + '?start=' + str(cast['nextPageTimestamp']) + '&end=' + str(end) + '&hostility=1&translate=true&' + token
		ucob = await ucobhandle(url, code, end, ucob, ucobt, token)
	else:
		if ucobt.gold > 4 or ucobt.enrage == 1:
			ucob.enrage += 1
		if ucobt.gold > 0:
			ucob.gold += 1
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

async def uwuhandle(url, code, end, uwu, uwut, token):
	data = requests.get(url)
	if data.status_code != 200:
		return uwu
	cast = data.json()
	for c in cast['events']:
		if not (c['ability'] is None):
			if c['ability']['name'] == 'Attack':
				continue
			elif c['ability']['name'] == 'Tumult':
				continue
			elif  c['ability']['name'] == '':
				continue
			if c['ability']['name'] == 'Sabik':
				uwut.enrage = 1
			elif c['ability']['name'] == 'Ultimate Suppression':
				uwut.supp = 1
			elif c['ability']['name'] == 'Ultimate Annihilation':
				uwut.annh = 1
			elif c['ability']['name'] == 'Ultimate Predation':
				uwut.pred = 1
			elif c['ability']['name'] == 'Ultima':
				uwut.ultima += 1
			elif c['ability']['name'] == 'Freefire':
				uwut.inter = 1
			elif c['ability']['name'] == 'Earthen Fury':
				uwut.titan = 1
			elif c['ability']['name'] == 'Hellfire':
				uwut.ifrit = 1
			#print(c['ability']['name'])
	if not (cast.get('nextPageTimestamp') is None):
		url = ulturl + code + '?start=' + str(cast['nextPageTimestamp']) + '&end=' + str(end) + '&hostility=1&translate=true&' + token
		uwu = await uwuhandle(url, code, end, uwu, uwut, token)
	else:
		uwu.enrage += uwut.enrage
		if uwut.ultima >= 4: #This seems to be weird? Every use equals to 2 casts for some reason.
			uwu.roul += 1
		uwu.supp += uwut.supp
		uwu.annh += uwut.annh
		uwu.pred += uwut.pred
		if uwut.ultima > 0:
			uwu.ultima += 1
		uwu.inter += uwut.inter
		uwu.titan += uwut.titan
		uwu.ifrit += uwut.ifrit
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

async def print_logs(encounter, message, start, code):
	text = ''
	start = int(start)

	for enc in encounter:
		enc.raidlen = round(enc.raidlen / 1000)
		enc.maxlen = round(enc.maxlen / 1000)
		if enc.pulls == 0:
			enc.pulls = 1
		text = '```*' + enc.raidtype + '*'
		text += '\nReport ID:	  ' + code
		text += '\nTotal pulls:	' + str(enc.pulls)
		text += '\nStart time:	 ' + datetime.fromtimestamp((start + enc.start) / 1000).strftime(dformat)
		text += '\nEnd time:	   ' + datetime.fromtimestamp((start + enc.end) / 1000).strftime(dformat)
		text += '\nTotal kills:	' + str(enc.kills)
		text += '\nRaid length:	' + str(await hhmmss(floor(enc.raidlen)))
		text += '\nPull length:	' + str(await hhmmss(floor(enc.rpullen / 1000)))
		text += '\nMax pull len:   ' + str(await hhmmss(enc.maxlen))
		text += '\nAvg pull len:   ' + str(await hhmmss(floor(enc.rpullen / 1000 / enc.pulls)))
		if enc.raidtype == 'The Epic of Alexander (Ultimate)':
			tea = enc.tea
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
			ucob = enc.ucob
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
			print(str(enc.pulls) + ' ' + str(ucob.nael) + ' ' + str(ucob.baha) + ' ' + str(ucob.quick) + ' ' + str(ucob.blck) + ' ' + str(ucob.fell) + ' ' + str(ucob.fall) + ' ' + str(ucob.ten) + ' ' + str(ucob.octet) + ' ' + str(ucob.doub) + ' ' + str(ucob.gold) + ' ' + str(ucob.enrage))
		elif enc.raidtype == "the Weapon\'s Refrain (Ultimate)" or enc.raidtype == 'The Weapon\'s Refrain (Ultimate)':
			uwu = enc.uwu
			text += '\n\nAdditional UWU information - Wipes by phase:'
			text += '\nGaruda: ' + str(enc.pulls - uwu.ifrit)
			text += ' Ifrit: ' + str(uwu.ifrit - uwu.titan)
			text += ' Titan: ' + str(uwu.titan - uwu.inter)
			text += ' LBs: ' + str(uwu.inter - uwu.ultima)
			text += ' Ultima: ' + str(uwu.ultima - uwu.pred)
			text += ' Pred: ' + str(uwu.pred - uwu.annh)
			text += ' Annih: ' + str(uwu.annh - uwu.supp)
			text += ' Supp: ' + str(uwu.supp - uwu.roul)
			text += ' Roul: ' + str(uwu.roul - uwu.enrage)
			text += ' Enrage: ' + str(uwu.enrage - enc.kills)
			print(str(enc.pulls) + ' ' + str(uwu.ifrit) + ' ' + str(uwu.titan) + ' ' + str(uwu.inter) + ' ' + str(uwu.pred) + ' ' + str(uwu.annh) + ' ' + str(uwu.supp) + ' ' + str(uwu.roul) + ' ' + str(uwu.enrage))
		text += '```'
		await message.channel.send(text)

async def addphase_check(report, enc):
	for p in report['enemies']:
		if p['name'] == 'Twintania':
			for g in p['fights']:
				if g.get('groups') is None:
					continue
				if g['groups'] >= 9 and g['id'] >= enc.fightid[0] and g['id'] <= enc.fightid[1]:
					enc.ucob.doub += 1
			break

async def parse_report(report, code, token, message):
	zone = ''
	enc = []
	i = 0
	enrage = False

	for p in report['fights']:
		if zone == '':
			enc.append(Report(p['zoneName']))
			zone = p['zoneName']
		elif p['zoneName'] != zone:
			if zone == 'the Unending Coil of Bahamut (Ultimate)':
				await addphase_check(report, enc[i])
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
				enrage = True
		if enc[i].fightid[0] == 0:
			enc[i].fightid[0] = p['id']
		enc[i].fightid[1] = p['id']
		enc[i].raidlen = enc[i].end - enc[i].start
		if enc[i].pullen > 20000:
			url = ulturl + code + '?start=' + str(p['start_time']) + '&end=' + str(p['end_time']) + '&hostility=1&translate=true&' + token
			if enc[i].raidtype == 'The Epic of Alexander (Ultimate)':
				enc[i].tea = await alexhandle(url, code, p['end_time'], enc[i].tea, TEA(enrage), token)
			elif enc[i].raidtype == 'the Unending Coil of Bahamut (Ultimate)':
				enc[i].ucob = await ucobhandle(url, code, p['end_time'], enc[i].ucob, UCoB(enrage), token)
			elif enc[i].raidtype == 'the Weapon\'s Refrain (Ultimate)' or enc[i].raidtype == 'The Weapon\'s Refrain (Ultimate)':
				enc[i].uwu = await uwuhandle(url, code, p['end_time'], enc[i].uwu, UWU(enrage), token)
		enrage = False
	if zone == 'the Unending Coil of Bahamut (Ultimate)':
		await addphase_check(report, enc[i])
	await print_logs(enc, message, report['start'], code)

async def get_pulls(message, code, token):
	if len(code) != 16:
		await message.channel.send('Invalid log!')
		return
	data = requests.get(logreport + code + '?' + token)
	if data.status_code != 200:
		await message.channel.send('There\'s an issue on FFlogs side or bad link: ' + str(data.status_code))
		return
	await parse_report(data.json(), code, token, message)
		