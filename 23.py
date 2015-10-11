#!/usr/bin/python
# coding:utf-8

import re


def main():

    rep = re.compile(r"==.*==")

    with open('jawiki-uk.txt', 'r') as fi:
        for line in fi.readlines():
            m = rep.match(unicode(line, 'utf-8'))
            if m is None:
                continue
            for l in xrange(3, 0, -1):
                if m.group()[: l + 1] == "=" * (l + 1):
                    print m.group()[l + 1: -(l + 1)].strip(), l
                    break


if __name__ == '__main__':
    main()
