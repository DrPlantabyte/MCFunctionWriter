#!/usr/bin/python3.8

import sys
import mcfunctions
from mcfunctions.mc16.commands import *
from mcfunctions.mc16.util import *

print('# Testing high-level API v0.1')

mcfunctions.set_output(print) # default: print output
# mcfunctions.set_output(None) # no output
# mcfunctions.set_output('myfunction.mcfuntion') # append/create file
#fh = open('myfunction2.mcfuntion','w')
#mcfunctions.set_output(fh) # use provided output stream

say('Regroup!')
teleport('@a', (0, '~', 0)) # all commands return string and write to set source
fill(('~-3', '~-1', '~-3'), ('~3', '~3', '~3'), 'glass', dest='keep')
fill(('~-2', '~', '~-2'), ('~2', '~2', '~2'), 'air')
setblock(('~', '~4', '~'), 'glowstone', dest='destroy')
tp('@r', ('~', '~5', '~'))
new_scoreboard('highscore', criteria='dummy', displayname='High Score', setdisplay='sidebar')
scoreboard_set_score(scoreboard='highscore', target='@a', amount=0)
scoreboard_add_score(scoreboard='highscore', target='@a', amount=1)
scoreboard_remove('highscore')
spawnpoint('@a', (0, '~', 0), angle=270)
tell('@r', "You're it!")
weather('clear', seconds=1000)
gamemode('survival', target='@a')
gamerule('keepInventory',True)
give('@a', 'cookie', count=13)
kill('@e[type=!player]')
spreadplayers(center=(0,0), spreadDistance=64, maxRange=500, respectTeams=True, target='@a')
clear('@r', item='cookie', maxCount=1)
clone( (0,0,0),(10,10,10),(20,70,5), copyAirBlocks=False, mode='force')
effect_give('@a', 'minecraft:speed', seconds=15, amplifier=2, showParticles=False)
effect_clear('@a', 'minecraft:haste')
enchant( '@r', 'sharpness', level=2)
forceload_add((0,0), to=(30,30))
forceload_remove((0,0), to=(30,30))
forceload_remove_all()

#fh.close()