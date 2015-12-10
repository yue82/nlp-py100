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

    y = np.array([c for c in worddic.values()])

    plt.hist(y, bins=500, range=(0, 10000))
    plt.ylabel('Frequency')
    plt.ylabel('Class')
    plt.savefig('38.png')
    plt.show()

if __name__ == '__main__':
    main()
