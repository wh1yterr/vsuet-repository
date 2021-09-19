# -- coding: utf-8 --
n = int(input())
m = n % (60 * 24) // 60
z = n % 60
if (n >= 0) and (n <= 1380) and (z >= 0) and (z <= 59) and (m >= 0) and (m <= 23):
  print(m ,'часов', z,'минут')