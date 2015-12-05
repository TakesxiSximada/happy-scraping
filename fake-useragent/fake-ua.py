#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse

import requests
from fake_useragent import UserAgent


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='http://127.0.0.1:8000/')
    args = parser.parse_args(argv)

    ua = UserAgent()
    headers = {
        'User-Agent': ua.chrome,
    }
    res = requests.get(args.url, headers=headers)
    print(res.request.headers)

if __name__ == '__main__':
    sys.exit(main())
