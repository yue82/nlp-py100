# coding:utf-8


class Morph():
    surface = u''
    base = u''
    pos = u''
    pos1 = u''

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '/'.join(self.utflist())

    def utflist(self):
        return [self.surface.encode('utf-8'),
                self.base.encode('utf-8'),
                self.pos.encode('utf-8'),
                self.pos1.encode('utf-8')]


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


class CabochaReader:

    def read_cabocha_f1(self, infile):
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

                elif uni_line[:2] == u'* ':
                    continue

                else:
                    surface, info = uni_line.split(u'\t')
                    pos, pos1 = info.split(u',')[:2]
                    base = info.split(u',')[-3]
                    morph = Morph(surface, base, pos, pos1)
                    seq.append(morph)
        return full_seq
