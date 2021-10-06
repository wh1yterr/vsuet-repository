# -- coding: utf-8 --
n = int(input())
m = int(input())
k = int(input())
def F(n,m,k):
   if(n * m > k and (k % m == 0 or k % n == 0)):
        return "Yes"
    else:
        return "No"
print(F(n,m,k))
