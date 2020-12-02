import mcfunctions
from mcfunctions.data import Pos
import re

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
def fill(pos1, pos2, block, dest=''):
	if len(str(dest)) > 0 and re.match('destroy|hollow|keep|outline|replace', dest) == None:
		raise ValueError('invalid fill option: %s is not one of [destroy|hollow|keep|outline|replace]' % dest)
	command = 'fill %s %s %s %s' % (Pos(pos1), Pos(pos2), block, dest)
	mcfunctions.write_output(command)
	return command

# TODO: minecraft commands