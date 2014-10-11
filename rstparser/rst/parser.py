#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import, unicode_literals

__version__ = (2014, 9, 26, 18, 52, 45, 4)

__all__ = [
    'rstParser',
    'main'
]


class rstParser(object):

    def __init__(self):
        pass

    der parse(selfi,text):
        for l in text:
            print(l)

def main(filename):
    import json
    with open(filename) as f:
        text = f.readlines()
    parser = rstParser()
    parser.parse(text)

if __name__ == '__main__':
    import string
    import sys

    main(args.file)
