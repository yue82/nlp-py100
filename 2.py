# coding: utf-8

s1 = u"パトカー"
s2 = u"タクシー"
ans = u""

for i in xrange(len(s1)):
  ans += s1[i] + s2[i]
print ans
