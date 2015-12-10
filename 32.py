#!/usr/bin/python
# coding:utf-8

from tools import MecabReader


def main():
    mr = MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for seq in full_seq:
        for morph in seq:
            if morph['pos'] == u'動詞':
                print morph['base']

if __name__ == '__main__':
    main()
