#!/usr/bin/python
# coding:utf-8

import MecabTools

def main():
    mr = MecabTools.MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for seq in full_seq:
        for morph in seq:
            if morph['pos'] == u'名詞' and morph['pos1'] == u'サ変接続':
                print morph['base']

if __name__ == '__main__':
   main()
