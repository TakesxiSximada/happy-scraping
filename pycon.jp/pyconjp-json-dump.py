#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import bs4
import requests

url = 'https://pycon.jp/2015/ja/schedule/tutorials/list/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text)
titles = [[elm.text, elm.get('href')] for elm in soup.select('.presentation h3 a')]
data = json.dumps(titles, ensure_ascii=False, indent=2, sort_keys=True)
with open('test.json', 'w+b') as fp:
    fp.write(data.encode('utf8'))
