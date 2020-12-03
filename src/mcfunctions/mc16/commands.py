import mcfunctions
from mcfunctions.data import Pos
import re, json

def say(msg):
	command = 'say %s' % msg
	return mcfunctions.write_output(command)
def tp(*args, **kwargs):
	teleport(*args, **kwargs)
def teleport(selector, pos):
	command = 'tp %s %s' % (selector, Pos(pos))
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
def scoreboard_add_score(selector, scoreboard, amount):
	command = 'scoreboard players add %s %s %s' % (selector, scoreboard, amount)
	return mcfunctions.write_output(command)
def scoreboard_subtract_score(selector, scoreboard, amount):
	command = 'scoreboard players remove %s %s %s' % (selector, scoreboard, amount)
	return mcfunctions.write_output(command)
def scoreboard_set_score(selector, scoreboard, amount):
	command = 'scoreboard players set %s %s %s' % (selector, scoreboard, amount)
	return mcfunctions.write_output(command)
def spawnpoint(selector, pos, angle=None):
	command = 'spawnpoint %s %s' % (selector, Pos(pos))
	if angle is not None:
		a = float(angle)
		while a < -180:
			a += 360
		while a > 180:
			a -= 360
		command += ' %.3f' % a
	return mcfunctions.write_output(command)
def tell(selector, message):
	return mcfunctions.write_output('tell %s %s'%(selector, message))
def weather(new_weather, seconds=None):
	if re.match('clear|rain|thunder', new_weather) == None:
		raise ValueError('invalid weather option: %s is not one of [clear|rain|thunder]' % new_weather)
	command = 'weather %s' % new_weather
	if seconds is not None:
		command += ' %s' % int(seconds)
	return mcfunctions.write_output(command)
def gamemode(mode, selector):
	if re.match('adventure|creative|spectator|survival', mode) == None:
		raise ValueError('invalid gamemode option: %s is not one of [adventure|creative|spectator|survival]' % mode)
	return mcfunctions.write_output('gamemode %s %s' % (mode, selector))
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
def give(selector, item, data=None, count=None):
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
		return mcfunctions.write_output('give %s %s %s' % (selector, istr, count))
	else:
		return mcfunctions.write_output('give %s %s' % (selector, istr))
def kill(selector):
	return mcfunctions.write_output('kill %s' % selector)
def spreadplayers(center, spread_distance, max_range, respect_teams=True, selector='@a'):
	return mcfunctions.write_output('spreadplayers %s %s %s %s %s' % (center, spread_distance, max_range, str(bool(respect_teams)).lower(), selector))

# TODO: minecraft commands