# -- coding: utf-8 --
n = int(input())
d = 0
d1 = 1
for i in range(1, n+1):
    d2 = d + d1
    d = d1
    d1 = d2
print(d2)
