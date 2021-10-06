# -- coding: utf-8 --
n = int(input())
kk = 1
s = 0
for i in range(1, n + 1):
  kk *= i
  s += kk
print(s)
