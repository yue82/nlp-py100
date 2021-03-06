#!/usr/bin/python
# coding:utf-8


class MecabReader:

    def read_mecab(self, infile):
        full_seq = []
        with open(infile, 'r') as fi:
            seq = []
            for line in fi.readlines():
                uni_line = unicode(line, 'utf-8')

                if uni_line.strip() == u'EOS':
                    if len(seq) != 0:
                        full_seq.append(seq)
                        seq = []
                    continue

                surface, info = uni_line.split(u'\t')
                pos, pos1 = info.split(u',')[:2]
                base = info.split(u',')[-3]
                morph = {
                    u'surface': surface,
                    u'base': base,
                    u'pos': pos,
                    u'pos1': pos1,
                }
                seq.append(morph)
        return full_seq


def main():
    mr = MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    for s in full_seq:
        for ss in s:
            for k, v in ss.items():
                print k, v,
            print ''


# if __name__ == '__main__':
#     main()
