# coding : utf-8
import sys

argvs = sys.argv
n =int(argvs[1])
fi = open("hightemp.txt", "r")
l = len([None for line in fi])/n
fi.close()

fi = open("hightemp.txt", "r")

for i in xrange(n-1):
  fo = open("split-" + str(i) + ".txt", "w")  
  for j in xrange(l):
    s = fi.readline()
    fo.write(s)
  fo.close()
  
fo = open("split-" + str(n-1) + ".txt", "w")  
while True: 
  s = fi.readline()
  if not s:
    break
  fo.write(s)
fo.close()
fi.close()
