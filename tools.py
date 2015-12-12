# coding:utf-8


class Morph(object):

    def __init__(self, *args):
        if len(args) == 4:
            self.surface, self.base, self.pos, self.pos1 = args
        else:
            self.surface = self.base = self.pos = self.pos1 = u''

    def __str__(self):
        return '/'.join(self.utf_attr())

    def utf_attr(self):
        return [elem.encode('utf-8') for elem in self.get_attr()]

    def get_attr(self):
        return [self.surface, self.base, self.pos, self.pos1]


class Chunk(object):

    def __init__(self, *args):
        self.morphs = []
        self.srcs = []
        if len(args) == 3:
            self.myindex = args[0]
            self.morphs.append(args[1])
            self.dst = args[2]
        else:
            self.myindex = 0
            self.dst = 0

    def __str__(self):
        return '/'.join(self.utf_attr())

    def utf_attr(self):
        return [elem.encode('utf-8') for elem in self.get_attr()]

    def get_attr(self):
        return [str(self.myindex),
                ' '.join([m.surface for m in self.morphs]),
                str(self.dst),
                '[' + ','.join([str(s) for s in self.srcs]) + ']']

    @classmethod
    def set_srcs(cls, chunks):
        for i, chunk in enumerate(chunks):
            dst = chunk.dst
            if dst >= 0:
                (chunks[dst].srcs).append(i)


class MecabReader(object):

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


class CabochaReader(object):

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

    def read_chunks(self, infile):
        full_chunks = []
        count = 0
        with open(infile, 'r') as fi:
            chunks = []
            chunk = None
            for line in fi.readlines():
                uni_line = unicode(line, 'utf-8')
                if uni_line.strip() == u'EOS':
                    if len(chunks) != 0:
                        if chunk is not None:
                            chunks.append(chunk)
                            chunk = None
                        Chunk.set_srcs(chunks)
                        full_chunks.append(chunks)
                        chunks = []

                elif uni_line[:2] == u'* ':
                    if chunk is not None:
                        chunks.append(chunk)
                        chunk = None
                    infos = uni_line[2:].split(' ')
                    myindex = int(infos[0])
                    dst = int(infos[1][:-1])
                else:
                    surface, info = uni_line.split(u'\t')
                    pos, pos1 = info.split(u',')[:2]
                    base = info.split(u',')[-3]
                    morph = Morph(surface, base, pos, pos1)
                    if chunk is None:
                        chunk = Chunk(myindex, morph, dst)
                    else:
                        chunk.morphs.append(morph)
        print count
        return full_chunks
