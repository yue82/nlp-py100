#coding:utf-8

fi = open("hightemp.txt", "r")
llist=[]
countdic={}
linedic={}

for line in fi.readlines():
  key = unicode(line, "utf-8").strip().split()[0]

  if linedic.has_key(key):
    countdic[key] += 1
    linedic[key].append(unicode(line, "utf-8"))
  else:
    countdic[key] = 1
    newlist = [unicode(line, "utf-8")]
    linedic[key] = newlist
fi.close()

fo = open("ans19.txt", "w")
for i in sorted(countdic.items(), key=lambda x:x[1], reverse=True):
  for v in linedic[i[0]]:
    fo.write(v.encode("utf-8"))

fo.close()
