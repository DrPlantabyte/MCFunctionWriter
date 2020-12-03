import mcfunctions
from mcfunctions.data import Pos
import re, json

def say(msg):
	command = 'say %s' % msg
	mcfunctions.write_output(command)
	return command
def tp(*args, **kwargs):
	teleport(*args, **kwargs)
def teleport(selector, pos):
	command = 'tp %s %s' % (selector, Pos(pos))
	mcfunctions.write_output(command)
	return command
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
	mcfunctions.write_output(command)
	return command
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
	mcfunctions.write_output(command)
	return command
def scoreboard_new(score_name, criteria='dummy', displayname=None):
	# example: /scoreboard objectives add highscore minecraft.custom:minecraft.time_since_death "High Score"
	command = 'scoreboard objectives add %s %s' % (score_name, criteria)
	if displayname is not None:
		command += ' "%s"' % displayname
	mcfunctions.write_output(command)
	return command
def scoreboard_remove(score_name):
	command = 'scoreboard objectives remove %s' % score_name
	mcfunctions.write_output(command)
	return command
def scoreboard_setdisplay(score_name, display='sidebar'):
	# setting a display a second time removes it
	command = 'scoreboard objectives setdisplay %s %s' % (display, score_name)
	mcfunctions.write_output(command)
	return command
def scoreboard_add_score(selector, score_name, amount):
	command = 'scoreboard players add %s %s %s' % (selector, score_name, amount)
	mcfunctions.write_output(command)
	return command
def scoreboard_subtract_score(selector, score_name, amount):
	command = 'scoreboard players remove %s %s %s' % (selector, score_name, amount)
	mcfunctions.write_output(command)
	return command
def scoreboard_set_score(selector, score_name, amount):
	command = 'scoreboard players set %s %s %s' % (selector, score_name, amount)
	mcfunctions.write_output(command)
	return command
# TODO: minecraft commands