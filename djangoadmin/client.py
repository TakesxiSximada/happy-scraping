#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getpass
import argparse
import urllib.parse

import requests
from bs4 import BeautifulSoup


class ScrapingError(Exception):
    pass


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--endpoint', default='http://127.0.0.1:8000/admin')
    parser.add_argument('username')
    args = parser.parse_args(argv)

    url = args.endpoint
    username = args.username
    password = getpass.getpass('password: ')
    res = requests.get(url)
    cookies = res.cookies
    soup = BeautifulSoup(res.content, 'lxml')

    forms = soup.select('form')
    if not forms:
        raise ScrapingError('no form')
    form = forms[0]

    params = {
        'csrfmiddlewaretoken': None,
        'username': username,
        'password': password,
    }

    urlobj = urllib.parse.urlparse(res.request.url)

    # CSRF token
    input_tags = form.select('input')
    for input_tag in input_tags:
        name = input_tag.get('name')
        if name == 'csrfmiddlewaretoken':
            params['csrfmiddlewaretoken'] = input_tag.get('value')
    target_url = '{}://{}{}{}'.format(
        urlobj.scheme,
        urlobj.hostname,
        (':{}'.format(urlobj.port) if urlobj.port else ''),
        form.get('action'),
    )
    res = requests.post(target_url, data=params, cookies=cookies)
    print(res.content)
    with open('res.html', 'w+b') as fp:
        fp.write(res.content)


if __name__ == '__main__':
    sys.exit(main())
