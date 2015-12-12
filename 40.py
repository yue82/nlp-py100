#!/usr/bin/python
# coding:utf-8

from tools import Morph
from tools import CabochaReader


def main():
    cr = CabochaReader()
    full_seq = cr.read_cabocha_f1('neko.txt.cabocha')
    for morph in full_seq[2]:
        print morph


if __name__ == '__main__':
    main()
