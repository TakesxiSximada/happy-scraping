#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import argparse
import requests
from bs4 import BeautifulSoup


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'))
    args = parser.parse_args(argv)

    url = 'https://pypi.python.org/pypi'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    records = soup.select('div.section table.list tr')
    iter_records = iter(records)
    next(iter_records)  # table header

    data = []
    for record in iter_records:
        tds = record.findAll('td')
        if tds[0].get('id') == 'last':
            break
        atag = tds[1].find('a')
        data.append({
            'title': atag.text,
            'url': atag.get('href'),
            'description': tds[2].text,
        })

    json.dump(data, args.output)

if __name__ == '__main__':
    sys.exit(main())
