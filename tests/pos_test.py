from mcfunctions.data import Pos

p1 = Pos('~1 64 ~0')
p2 = p1 + (10,20,30)
print(p1)
print(p2-p1)
print(p1 * 2)
print(p1 / 2)
print(p1 // 2)