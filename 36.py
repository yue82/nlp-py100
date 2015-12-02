#!/usr/bin/python
# coding:utf-8

import MecabTools


def main():
    mr = MecabTools.MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    worddic = {}
    for seq in full_seq:
        l = []
        for morph in seq:
            if morph['pos'] == u'記号':
                continue
            if morph['surface'] in worddic:
                worddic[morph['surface']] += 1
            else:
                worddic[morph['surface']] = 1

    rank = sorted(worddic.items(), key = lambda x: x[1])[::-1]
    for word in rank:
        print word[0], word[1]


if __name__ == '__main__':
    main()
