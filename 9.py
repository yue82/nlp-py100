# coding: utf-8
import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ss = s.split(" ")
ans = []   
for i in xrange(len(ss)):
    if len(ss[i]) > 4:
        a = ss[i][0]
        for r in random.sample(ss[i][1:], len(ss[i])-1):
            a += r
        ans.append(a)
    else:
        ans.append(ss[i])
print " ".join(ans)
