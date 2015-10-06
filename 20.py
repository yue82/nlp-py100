#!/usr/bin/python
# coding:utf-8

import json


def main():
    data = {}
    with open('jawiki-country.json', 'r') as f:
        for line in f.readlines():
            data[len(data)] = json.loads(line)

    for v in data.values():
        if v["title"] == u'イギリス':
            print v["text"]


if __name__ == '__main__':
    main()
