from .commands import *

def new_scoreboard(score_name, criteria='dummy', displayname=None, setdisplay=None):
	commands = []
	commands.append(scoreboard_new(score_name=score_name, criteria=criteria, displayname=displayname))
	if setdisplay is not None:
		commands.append(scoreboard_setdisplay(score_name=score_name, setdisplay=setdisplay))
	return '\n'.join(commands)

def sphere(center, radius):
	# TODO
	pass

def place_command_block(pos, command, facing='down', conditional=False, type='impulse'):
	# TODO
	raise Exception('W.I.P.')
def place_impulse_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='impulse')
def place_chain_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='chain')
def place_repeating_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='repeat')