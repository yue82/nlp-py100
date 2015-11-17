#!/usr/bin/python
# coding:utf-8

import MecabTools

def main():
    mr = MecabTools.MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for seq in full_seq:
        for morph in seq:
            if morph['pos'] == u'動詞':
                print morph['base']

if __name__ == '__main__':
   main()
