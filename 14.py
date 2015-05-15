# coding : utf-8
import sys

argvs = sys.argv
fi = open("hightemp.txt", "r")
for s in fi.readlines()[:int(argvs[1])]:
  print s.strip()
  
