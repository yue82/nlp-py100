#!/usr/bin/python
# coding:utf-8

def read_mecab(infile):
    test_count = 0
    full_seq = []
    with open(infile, 'r') as fi:
        seq = []
        for line in fi.readlines():
            uni_line = unicode(line, 'utf-8')

            if uni_line.strip() == u'EOS':
                if len(seq) != 0:
                    full_seq.append(seq)
                    seq = []
                    if test_count == 2:
                        break
                    test_count += 1
                continue

            surface, info = uni_line.split(u'\t')
            base, pos, pos1 = info.split(u',')[:3]
            org = info.split(u',')[-3]
            morph = {(surface, base, pos, pos1):org}
            seq.append(morph)

    # print full_seq

def main():
    read_mecab('neko.txt.mecab')


if __name__ == '__main__':
   main()
