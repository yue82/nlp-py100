#!/usr/bin/python
# coding:utf-8

from tools import MecabReader
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm


def main():
    mr = MecabReader()
    full_seq = mr.read_mecab('neko.txt.mecab')
    worddic = {}
    for seq in full_seq:
        l = []
        for morph in seq:
            if morph['pos'] == u'記号':
                continue
            if morph['surface'] in worddic:
                worddic[morph['surface']] += 1
            else:
                worddic[morph['surface']] = 1

    rank = sorted(worddic.items(), key=lambda x: x[1])[::-1]
    top10 = rank[:10]

    x = np.array([i for i in range(len(top10))])
    y = np.array([w[1] for w in top10])
    fp = fm.FontProperties(
        fname='/usr/share/fonts/truetype/fonts-japanese-gothic.ttf')

    plt.bar(x, y)
    plt.xticks(x + 0.5, [w[0] for w in top10], fontproperties=fp)
    plt.ylabel('word count')
    plt.ylabel('top 10')
    plt.savefig('37.png')
    plt.show()

if __name__ == '__main__':
    main()
