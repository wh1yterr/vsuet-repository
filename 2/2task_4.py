# -- coding: utf-8 --
a = int(input())
b = int(input())
l = int(input())
N = int(input())
def i(a,b,l,N):
  return (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
print(i(a,b,l,N))