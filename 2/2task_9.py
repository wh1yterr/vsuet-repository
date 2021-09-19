# -- coding: utf-8 --
n = int(input())
m = int(input())
k = int(input())
k1 = 0
def F(n,m,k,k1):
  k1 = (n*m) / 2
  if (k1==k):
    return 'yes'
  elif (k1!=k): return 'no'
print(F(n,m,k,k1))