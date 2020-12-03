import mcfunctions
from mcfunctions.data import Pos
import re, json

def say(msg):
	command = 'say %s' % msg
	return mcfunctions.write_output(command)
def tp(*args, **kwargs):
	teleport(*args, **kwargs)
def teleport(target, pos):
	command = 'tp %s %s' % (target, Pos(pos))
	return mcfunctions.write_output(command)
def fill(pos1, pos2, block, blockstate=None, data=None, dest=''):
	if len(str(dest)) > 0 and re.match('destroy|hollow|keep|outline|replace', dest) == None:
		raise ValueError('invalid fill option: %s is not one of [destroy|hollow|keep|outline|replace]' % dest)
	blockstr = block
	if blockstate is not None:
		blockstr += '['
		for key in blockstate:
			value = blockstate[key]
			blockstr += '%s=%s' % (key, value)
		blockstr += ']'
	if data is not None:
		if type(data) == str:
			if data.strip()[0] != '{':
				blockstr += '{%s}' % data.strip()
			else:
				blockstr += data.strip()
		else:
			blockstr += json.dumps(data)
	command = 'fill %s %s %s %s' % (Pos(pos1), Pos(pos2), blockstr, dest)
	command = command.strip()
	return mcfunctions.write_output(command)
def setblock(pos,block, blockstate=None, data=None, dest=''):
	if len(str(dest)) > 0 and re.match('destroy|keep|replace', dest) == None:
		raise ValueError('invalid fill option: %s is not one of [destroy|keep|replace]' % dest)
	blockstr = block
	if blockstate is not None:
		blockstr += '['
		for key in blockstate:
			value = blockstate[key]
			blockstr += '%s=%s' % (key, value)
		blockstr += ']'
	if data is not None:
		if type(data) == str:
			if data.strip()[0] != '{':
				blockstr += '{%s}' % data.strip()
			else:
				blockstr += data.strip()
		else:
			blockstr += json.dumps(data)
	command = 'setblock %s %s %s' % (Pos(pos), blockstr, dest)
	command = command.strip()
	return mcfunctions.write_output(command)
def scoreboard_new(scoreboard, criteria='dummy', displayname=None):
	# example: /scoreboard objectives add highscore minecraft.custom:minecraft.time_since_death "High Score"
	command = 'scoreboard objectives add %s %s' % (scoreboard, criteria)
	if displayname is not None:
		command += ' "%s"' % displayname
	return mcfunctions.write_output(command)
def scoreboard_remove(scoreboard):
	command = 'scoreboard objectives remove %s' % scoreboard
	return mcfunctions.write_output(command)
def scoreboard_setdisplay(scoreboard, display='sidebar'):
	# setting a display a second time removes it
	command = 'scoreboard objectives setdisplay %s %s' % (display, scoreboard)
	return mcfunctions.write_output(command)
def scoreboard_add_score(target, scoreboard, amount):
	command = 'scoreboard players add %s %s %s' % (target, scoreboard, amount)
	return mcfunctions.write_output(command)
def scoreboard_subtract_score(target, scoreboard, amount):
	command = 'scoreboard players remove %s %s %s' % (target, scoreboard, amount)
	return mcfunctions.write_output(command)
def scoreboard_set_score(target, scoreboard, amount):
	command = 'scoreboard players set %s %s %s' % (target, scoreboard, amount)
	return mcfunctions.write_output(command)
def spawnpoint(target, pos, angle=None):
	command = 'spawnpoint %s %s' % (target, Pos(pos))
	if angle is not None:
		a = float(angle)
		while a < -180:
			a += 360
		while a > 180:
			a -= 360
		command += ' %.3f' % a
	return mcfunctions.write_output(command)
def tell(target, message):
	return mcfunctions.write_output('tell %s %s'%(target, message))
def weather(w, seconds=None):
	if re.match('clear|rain|thunder', w) == None:
		raise ValueError('invalid weather option: %s is not one of [clear|rain|thunder]' % w)
	command = 'weather %s' % w
	if seconds is not None:
		command += ' %s' % int(seconds)
	return mcfunctions.write_output(command)
def gamemode(mode, target):
	if re.match('adventure|creative|spectator|survival', mode) == None:
		raise ValueError('invalid gamemode option: %s is not one of [adventure|creative|spectator|survival]' % mode)
	return mcfunctions.write_output('gamemode %s %s' % (mode, target))
def gamerule(rule, setting):
	if type(setting) == str:
		setting = bool(setting)
	if type(setting) == int:
		setting = setting != 0
	if type(setting) != bool:
		raise ValueError('invalid boolean: %s should be either True or False' % setting)
	if setting == True:
		sstr = 'true'
	else:
		sstr = 'false'
	return mcfunctions.write_output('gamerule %s %s' % (rule, sstr))
def give(target, item, data=None, count=None):
	istr = item
	if data is not None:
		if type(data) == str:
			if data.strip()[0] != '{':
				istr += '{%s}' % data.strip()
			else:
				istr += data.strip()
		else:
			istr += json.dumps(data)
	if count is not None:
		return mcfunctions.write_output('give %s %s %s' % (target, istr, count))
	else:
		return mcfunctions.write_output('give %s %s' % (target, istr))
def kill(target):
	return mcfunctions.write_output('kill %s' % target)
def spreadplayers(center, spreadDistance, maxRange, respectTeams=True, target='@a'):
	return mcfunctions.write_output('spreadplayers %s %s %s %s %s' % (center, spreadDistance, maxRange, str(bool(respectTeams)).lower(), target))
def clear(target, item=None, maxCount=None):
	command = 'clear %s' % target
	if item is not None:
		command += ' %s' % item
	if maxCount is not None:
		command += ' %s' % maxCount
	return mcfunctions.write_output(command)
def clone( startPos, endPos, destPos, copyAirBlocks=True, mode='force'):
	if copyAirBlocks:
		mask = 'replace'
	else:
		mask = 'masked'
	if re.match('force|move|normal', mode) == None:
		raise ValueError('invalid clone mode option: %s is not one of [force|move|normal]' % mode)
	return mcfunctions.write_output('clone %s %s %s %s %s' % (Pos(startPos), Pos(endPos), Pos(destPos), mask, mode))
def effect_give(target, effect, seconds=None, amplifier=None, showParticles=True):
	hideParticles = not showParticles
	#effect give <targets> <effect> [<seconds>] [<amplifier>] [<hideParticles>]
	command = 'effect give %s %s' % (target, effect)
	if seconds is not None or amplifier is not None or hideParticles:
		if seconds == None:
			seconds = 30
		if amplifier is None:
			amplifier = 1
		command += ' %s %s %s' % (seconds, amplifier, str(hideParticles).lower())
	return mcfunctions.write_output(command)
def effect_clear(target, effect=None):
	if effect is None:
		return mcfunctions.write_output('effect clear %s' % target)
	else:
		return mcfunctions.write_output('effect clear %s %s' % (target, effect))

# TODO: minecraft commands