#!/usr/bin/python
# coding:utf-8

import re


def main():

    base_info_start = u'{{基礎情報'
    element_pattern = r'^\|(.+)=(.+)'
    base_info_end = u'}}'

    rep = re.compile(element_pattern)

    elements = {}

    with open('jawiki-uk.txt', 'r') as fi:
        uni_line = unicode(fi.readline(), 'utf-8')
        while uni_line[:6] != base_info_start:
            uni_line = unicode(fi.readline(), 'utf-8')

        key = ''
        for line in fi.readlines():
            uni_line = unicode(line, 'utf-8')
            if uni_line[:2] == base_info_end:
                break

            value = ''
            find = rep.finditer(uni_line)
            for match in find:
                key = match.groups()[0]
                value = match.groups()[1]

            if value == '':
                elements[key] += uni_line.strip()
            else:
                elements[key] = value

    for k, v in elements.items():
        print k, ':', v

if __name__ == '__main__':
    main()
