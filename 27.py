#!/usr/bin/python
# coding:utf-8

import re


def main():

    base_info_start = u'{{基礎情報'
    element_pattern = r'^\|(.+)=(.+)'
    base_info_end = u'}}'

    strong_pattern = r"([^']*)(''*)([^']+)?(''*)([^']*)"
    nol = r'([^\[\]\|]+)?'
    sep = r'(\|)?'
    link_pattern = nol + r'\[\[' + nol + sep + nol + sep + nol + r'\]\]' + nol

    rep = re.compile(element_pattern)
    rep2 = re.compile(strong_pattern)
    rep3 = re.compile(link_pattern)

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

        find = rep2.finditer(v)
        v1 = ''
        for match in find:
            m = match.groups()
            if m[0] != None:
                v1 += m[0]
            v1 += m[2]
            if m[2] != None:
                v1 += m[-1]
        if v1 == '':
            v1 = v

        find3 = rep3.finditer(v1)
        v2 = ''
        for match3 in find3:
            m = match3.groups()
            if m[0] is not None:
                v2 += m[0].strip()

            if m[-3] == u'|':
                v2 += m[-2].strip()
            elif m[3] == u'|':
                v2 += m[4].strip()
            else:
                v2 += m[1].strip()

            if m[-1] is not None:
                v2 += m[-1].strip()
        if v2 == '':
            v2 = v1

        elements[k] = v2

    for k, v in elements.items():
        print k, ':', v


if __name__ == '__main__':
    main()
