# coding: utf-8

# 5からそのまま
def getNgram(seq, n):
    ans = []
    for i in xrange(len(seq)-n+1):
        ans.append(seq[i:i+n])
    return ans

s1 = "paraparaparadise"
s2 = "paragraph"
x = set(getNgram(s1, 2))
y = set(getNgram(s2, 2))
print "union = " + str(list(x.union(y)))
print "intersection = " + str(list(x.intersection(y)))
print "difference = " + str(list(x.difference(y)))
if "se" in x:
    print "x has \"se\" "
if "se" in y:
    print "y has \"se\" "
