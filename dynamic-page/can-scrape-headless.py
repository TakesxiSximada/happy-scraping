#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from selenium.webdriver import PhantomJS as WebDriver


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default='http://127.0.0.1:8000/static/index.html')
    args = parser.parse_args(argv)

    url = args.url

    browser = WebDriver()
    browser.get(url)
    tags = browser.find_elements_by_css_selector('li')
    for tag in tags:
        print(tag.text)
    browser.close()

if __name__ == '__main__':
    sys.exit(main())
