# -- coding: utf-8 --
s = input()
s1 = s[:s.find('h')]
s2 = s[int(s.find('h')):int(s.rfind('h') + 1)]
s3 = s[s.rfind('h') + 1:]
print(s1 + s2[::-1] + s3)
