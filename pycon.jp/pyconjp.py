#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import json
import argparse

import bs4
import requests

TARGET_URL = 'https://pycon.jp/2015/ja/schedule/tutorials/list/'


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=argparse.FileType('w', encoding='utf-8'))
    parser.add_argument('-f', '--format', default='json', choices=['json', 'csv'])
    args = parser.parse_args(argv)

    fmt = args.format
    output = args.output

    res = requests.get(TARGET_URL)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    titles = [(elm.text, elm.get('href')) for elm in soup.select('.presentation h3 a')]

    if fmt == 'json':
        data = json.dumps(titles, ensure_ascii=False, indent=2, sort_keys=True)
        output.write(data)
    elif fmt == 'csv':
        writer = csv.writer(output)
        writer.writerows(titles)


if __name__ == '__main__':
    sys.exit(main())
