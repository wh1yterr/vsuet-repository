# -- coding: utf-8 --
x = int(input())
y = int(input())
z = int(input())
def F(x,y,z):
  if ((x == y) and (x == z)) or ((x == y) and (y == z)) or ((z == y) and (x == z)):
    return '3'
  elif (x == y) or (x == z) or (y == z):
    return '2'
  else: return '0'
print (F(x,y,z))