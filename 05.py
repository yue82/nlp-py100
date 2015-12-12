# coding: utf-8

def getNgram(seq, n):
    ans = []
    for i in xrange(len(seq)-n+1):
        ans.append(seq[i:i+n])
    return ans

s = "I am an NLPer"
print getNgram(s.split(" "), 2)
print getNgram(s, 2)
