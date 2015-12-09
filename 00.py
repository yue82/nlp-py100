#coding: utf-8
s = "stressed"
ans = ""
for i in xrange(len(s)):
  ans += s[-(i+1)]
print ans
