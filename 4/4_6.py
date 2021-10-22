# -- coding: utf-8 --
s = input()
t = s.find('f')
x = int(len(s))
if s.count('f') >= 2:
    print(int(s.find('f', t + 1, x)) + 1)
elif s.count('f') == 1:
      print('-1')
else:
    print('-2')
