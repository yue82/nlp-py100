#!/usr/bin/python
# coding:utf-8

import MecabTools

def main():
    mr = MecabTools.MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for seq in full_seq:
        before = ''
        got_A = False
        got_no = False
        for morph in seq:
            if morph['base'] == u'の' and got_A:
                got_no = True
                continue

            if morph['pos'] == u'名詞':
                if got_A and got_no:
                    print before + u' の ' + morph['base']
                    got_A = False
                else:
                    before = morph['base']
                    got_A = True
                got_no = False

            else:
                got_A = False

if __name__ == '__main__':
   main()
