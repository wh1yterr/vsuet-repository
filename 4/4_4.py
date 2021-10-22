# -- coding: utf-8 --
s = input()
c = int(s.find(' ')) + 1
b = int(len(s))
a = str(s[c:b]) + str(' ') + str(s[:c])
print(a)
