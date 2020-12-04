import mcfunctions
from mcfunctions.mc16.util import *

p1 = '~ ~50 ~'
mcfunctions.set_output('test2')
sphere(p1, 20, 'glass')
sphere(p1, 18, 'water')
cylinder('~ ~ ~', radius=3, height=25, block='glass')
cylinder('~ ~ ~', radius=1, height=25, block='air')