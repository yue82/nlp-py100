#!/usr/bin/python
# coding:utf-8

import re


def main():

    base_info_start = u'{{基礎情報'
    element_pattern = r'^\|(.+)=(.+)'
    base_info_end = u'}}'
    strong_pattern = r"([^']*)''(.+)''([^']*)"

    rep = re.compile(element_pattern)
    rep2 = re.compile(strong_pattern)

    elements = {}

    with open('jawiki-uk.txt', 'r') as fi:
        uni_line = unicode(fi.readline(), 'utf-8')
        while uni_line[:6] != base_info_start:
            uni_line = unicode(fi.readline(), 'utf-8')
        for line in fi.readlines():
            uni_line = unicode(line, 'utf-8')
            if uni_line[:2] == base_info_end:
                break
            find = rep.finditer(uni_line)
            for match in find:
                key = match.groups()[0]
                value = match.groups()[1]

                find2 = rep2.finditer(value)
                for match2 in find2:
                    v = match2.groups()[1]
                    if v[1] == u"'":
                        value = match2.groups()[0] + v[2:-2] + match2.groups()[2]
                    elif v[0] == u"'":
                        value = match2.groups()[0] + v[1:-1] + match2.groups()[2]
                    else:
                        value == match2.groups()[0] + v + match2.groups()[2]
                elements[key] = value

    for k, v in elements.items():
        print k, ':', v

if __name__ == '__main__':
    main()
