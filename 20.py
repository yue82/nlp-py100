#!/usr/bin/python
# coding:utf-8

import json


def main():
    data = {}
    with open('jawiki-country.json', 'r') as fi:
        for line in fi.readlines():
            data[len(data)] = json.loads(line)

    for v in data.values():
        if v["title"] == u'イギリス':
            print v["text"]
            with open('jawiki-uk.txt', 'w') as fo:
                fo.write(v["text"].encode('utf-8'))
            return

if __name__ == '__main__':
    main()
