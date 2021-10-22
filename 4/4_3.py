# -- coding: utf-8 --
s = input()
a = int(len(s))
b = int(len(s))//2 + 1
c = str(s[b:a]) + str(s[:b])
print(c)
