#!/usr/bin/python
# coding:utf-8

import re


def main():

    extensions = [r'jpg', r'png', r'svg']
    prefix1 = r'(:.*?\.)'
    prefix2 = r'(= .*?\.)'

    ex_pattern = r'('
    for ex in extensions + [ex.upper() for ex in extensions]:
        ex_pattern += r'(' + ex + r')|'
    ex_pattern = ex_pattern[:-1] + r')'

    rep = re.compile(prefix1 + ex_pattern)
    rep2 = re.compile(prefix2 + ex_pattern)

    medias = []

    with open('jawiki-uk.txt', 'r') as fi:
        for line in fi.readlines():
            uni_line = unicode(line, 'utf-8')
            f = rep.findall(uni_line)
            if len(f) > 0:
                for match in f:
                    medias.append(match[0][1:] + match[1])
            else:
                for match in rep2.findall(uni_line):
                    medias.append(match[0][2:] + match[1])

    for m in medias:
        print m

if __name__ == '__main__':
    main()
