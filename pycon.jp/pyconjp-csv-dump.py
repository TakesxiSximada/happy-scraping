#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import bs4
import requests

url = 'https://pycon.jp/2015/ja/schedule/tutorials/list/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text)
titles = [(elm.text, elm.get('href')) for elm in soup.select('.presentation h3 a')]
fp = open('test.csv', 'w+t')
writer = csv.writer(fp)
writer.writerows(titles)
fp.close()
