#coding: utf-8
import sys

def cipher(s):
    ans = ""
    for i in xrange(len(s)):
        if s[i].islower():
            ans += chr(219 - ord(s[i]))
        else:
            ans += s[i]
    return ans
            
s ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print s
print cipher(s)
        
