#!/usr/bin/python
# coding:utf-8

from tools import MecabReader


def main():
    mr = MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for seq in full_seq:
        l = []
        for morph in seq:
            if morph['pos'] == u'名詞':
                l.append(morph['base'])
            else:
                if len(l) > 1:
                    print '/'.join(l)
                    l = []
                else:
                    l = []
        if len(l) > 1:
            print '/'.join(l)

if __name__ == '__main__':
    main()
