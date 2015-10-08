#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json

with open('test.json', 'rt', encoding='utf8') as fp:
    title_url = json.load(fp)

for title, url in title_url:
    print('{}: {}'.format(title, url))
