# -- coding: utf-8 --
k = int(input())
n = int(input())
d = 0
d1 = 1
a = k + n
for i in range(1, a + 1):
    d2 = d + d1
    d = d1
    d1 = d2
print(d2)
