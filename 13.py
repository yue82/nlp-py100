# coding: utf-8
fi1 = open("col1.txt", "r")
fi2 = open("col2.txt", "r")
fo = open("merge.txt", "w")
fo.write(fi1.readline().strip() + "\t" + fi2.readline().strip())
fi1.close()
fi2.close()
fo.close()

