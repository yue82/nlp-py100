#coding:utf-8

fi = open("hightemp.txt", "r")
fset=set()

for line in fi.readlines():
    fset.add(unicode(line, "utf-8").strip().split()[0])    

for f in list(fset):
    print f

fi.close()
