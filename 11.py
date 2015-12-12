# coding: utf-8
f = open("hightemp.txt", "r")
for s in f.readlines():
    print " ".join(s.split("\t"))
f.close()
