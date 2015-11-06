#!/usr/bin/python
# coding:utf-8

import re
import urllib2
import json

def main():

    base_info_start = u'{{基礎情報'
    element_pattern = r'^\|([^=]+)?=(.+)'
    base_info_end = u'}}'

    flag_str = u'国旗画像'

    rep = re.compile(element_pattern)

    api_endpoint = 'https://ja.wikipedia.org/w/api.php'
    api_params1 = ['format=json', 'action=query']
    api_titles =  'titles=File:'
    api_params2 = ['prop=imageinfo', '&iiprop=url']

    title = None
    with open('jawiki-uk.txt', 'r') as fi:
        uni_line = unicode(fi.readline(), 'utf-8')
        while uni_line[:6] != base_info_start:
            uni_line = unicode(fi.readline(), 'utf-8')

        for line in fi.readlines():
            uni_line = unicode(line, 'utf-8')
            if uni_line[:2] == base_info_end:
                break

            find = rep.finditer(uni_line)
            for match in find:
                key = match.groups()[0].strip()
                value = match.groups()[1].strip()
                if key == flag_str:
                    title = value
                    break
            if title is not None:
                break

    url = api_endpoint
    url += '?' + '&'.join(api_params1)
    url += '&' + api_titles + title.replace(' ', '%20')
    url += '&' + '&'.join(api_params2)
    res = json.loads(urllib2.urlopen(url).read())

    imgurl = res[u'query'][u'pages'][u'-1'][u'imageinfo'][0][u'url']
    print imgurl

if __name__ == '__main__':
    main()
