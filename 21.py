#!/usr/bin/python
# coding:utf-8


def main():
    i = 0
    cate_lines = []
    with open('jawiki-uk.txt', 'r') as fi:
        for line in fi.readlines():
            i += 1
            if unicode(line, "utf-8")[:11] == u'[[Category:':
                cate_lines.append(i)

    print "Category Line:",
    for line in cate_lines:
        print line,

if __name__ == '__main__':
    main()
