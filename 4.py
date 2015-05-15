# coding: utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
oneAlph = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ss = s.split(" ")
ans = {}
for i in xrange(len(ss)):
    if i+1 in oneAlph:
        ans[ss[i][0]] = i+1
    else:
        ans[ss[i][0:2]] = i+1
print ans
