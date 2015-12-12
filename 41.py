#!/usr/bin/python
# coding:utf-8

from tools import Morph
from tools import Chunk
from tools import CabochaReader


def main():
    show_line = 8
    cr = CabochaReader()
    full_chunks = cr.read_chunks('neko-short.txt.cabocha')

    for chunk in full_chunks[show_line-1]:
        print chunk


if __name__ == '__main__':
    main()
