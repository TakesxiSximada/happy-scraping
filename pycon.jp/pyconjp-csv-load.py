#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv

fp = open('test.csv', 'rt', encoding='utf8')
reader = csv.reader(fp)
for row in reader:
    print('{}: {}'.format(row[0], row[1]))
fp.close()
