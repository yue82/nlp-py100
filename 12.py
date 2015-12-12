# coding: utf-8
fi = open("hightemp.txt", "r")
fo1 = open("col1.txt", "w")
fo2 = open("col2.txt", "w")
fo1.write(fi.readline().strip())
fo2.write(fi.readline().strip())
fi.close()
fo1.close()
fo2.close()

