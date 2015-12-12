#coding:utf-8

fi = open("hightemp.txt", "r")
flist=[]

for line in fi.readlines():
    flist.append(unicode(line, "utf-8").strip().split())
fi.close()

flist.sort(key=lambda x:(x[2]))

fo = open("ans18.txt", "w")    
for f in flist:
    s = u'\t'.join(f) + u'\n'
    fo.write(s.encode("utf-8"))
    
