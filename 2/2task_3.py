# -- coding: utf-8 --
n = int(input())
a = n % (60 * 24) // 60
b = n % 60
if (n <= 1440) and (b <= 59) and (a <= 24):
  print(a ,'hours', b,'minutes')
else:
  print('ERROR')