from .commands import *
import math

def new_scoreboard(name, criteria='dummy', displayname=None, setdisplay=None):
	commands = []
	commands.append(scoreboard_new(scoreboard=name, criteria=criteria, displayname=displayname))
	if setdisplay is not None:
		commands.append(scoreboard_setdisplay(scoreboard=name, display=setdisplay))
	return '\n'.join(commands)

def cylinder(baseCenter, radius, height, block, blockstate=None):
	if float(radius) == 0:
		return ''
	commands = []
	c = Pos(baseCenter).block_pos()
	r = float(radius)
	h = int(round(abs(height)))
	if height >= 0:
		dir = 1
	else:
		dir = -1
	if h == 0:
		h = 1
	if radius < 1.5:
		# special case, just a column
		return fill(c, c + (0, (h-1) * dir, 0), block=block, blockstate=blockstate)
	# work way around 1/8 of circle, and fill with symmetry
	# start at 0 degrees (+x), and rotate around until the int value of x changes, then do a fill and continue
	iter_angle = (1.0 / r) / 4
	angle = 0
	while angle < (math.pi / 4 + iter_angle):
		r_pos = (c + (r*math.cos(angle), 0, r*math.sin(angle))).block_pos()
		angle += iter_angle
		next_r_pos = (c + (r*math.cos(angle), 0, r*math.sin(angle))).block_pos()
		if r_pos.x != next_r_pos.x:
			# do a fill
			dx = int(r_pos.x - c.x)
			dy = (h-1) * dir
			dz = int(r_pos.z - c.z)
			commands.append(fill(c + (-dx, 0, -dz), c + (dx, dy, dz), block=block, blockstate=blockstate))
			if dx != dz:
				commands.append(fill(c + (-dz, 0, -dx), c + (dz, dy, dx), block=block, blockstate=blockstate))
	return '\n'.join(commands)
def sphere(center, radius, block, blockstate=None):
	if float(radius) == 0:
		return ''
	r = float(radius)
	commands = []
	last_radius = 0
	for dy in range (0, int(r)+1):
		angle = math.asin(dy/r)
		sub_radius = int(round(r * math.cos(angle)))
		if sub_radius != last_radius:
			commands.append(cylinder(baseCenter=Pos(center)-(0,dy,0), radius=sub_radius, height=dy * 2 + 1, block=block, blockstate=blockstate))
		last_radius = sub_radius
	return '\n'.join(commands)

def place_command_block(pos, command, facing='down', conditional=False, type='impulse'):
	# TODO
	raise Exception('W.I.P.')
def place_impulse_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='impulse')
def place_chain_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='chain')
def place_repeating_command_block(pos, command, facing='down', conditional=False):
	return place_command_block(pos=pos, command=command, facing=facing, conditional=conditional, type='repeat')