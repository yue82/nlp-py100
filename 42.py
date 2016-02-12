#!/usr/bin/python
# coding:utf-8

from tools import Morph
from tools import Chunk
from tools import CabochaReader


def main():
    cr = CabochaReader()
    full_chunks = cr.read_chunks('neko.txt.cabocha')

    for chunks in full_chunks:
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            print '\t'.join([chunk.str_morphs(),
                             chunks[chunk.dst].str_morphs()])


if __name__ == '__main__':
    main()
