#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import argparse
import requests
from bs4 import BeautifulSoup


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='http://127.0.0.1:8000/static/index.html')
    args = parser.parse_args(argv)

    url = args.url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    lis = soup.select('li')
    print(lis)

if __name__ == '__main__':
    sys.exit(main())
