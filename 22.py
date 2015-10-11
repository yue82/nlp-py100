#!/usr/bin/python
# coding:utf-8


def main():
    cates = []
    with open('jawiki-uk.txt', 'r') as fi:
        for line in fi.readlines():
            if unicode(line, "utf-8")[:11] == u'[[Category:':
                tmp1 = unicode(line, "utf-8").strip().split(':')[1]
                tmp2 = tmp1.split(']')[0]
                cate = tmp2.split('|')[0]
                cates.append(cate)

    print "Category:",
    for line in cates:
        print line,

if __name__ == '__main__':
    main()
