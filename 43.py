#!/usr/bin/python
# coding:utf-8

from tools import Morph
from tools import Chunk
from tools import CabochaReader


def main():
    cr = CabochaReader()
    full_chunks = cr.read_chunks('neko.txt.cabocha')

    for chunks in full_chunks[:10]:
        for chunk in chunks:
            if not has_pos(u'動詞', chunk):
                continue
            for src in chunk.srcs:
                if not has_pos(u'名詞', chunks[src]):
                    continue
                print '\t'.join([chunks[src].str_morphs(),
                                 chunk.str_morphs()])


def has_pos(pos, chunk):
    return pos in [m.pos for m in chunk.morphs]


if __name__ == '__main__':
    main()
