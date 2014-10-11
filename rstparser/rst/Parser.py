#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
from __future__ import absolute_import, unicode_literals

__version__ = (2014, 9, 26, 18, 52, 45, 4)

__all__ = [
    'Parser',
    'main'
]


class Parser(object):

    def __init__(self):
        pass

    def parse(self, text):
        for l in text:
            print(l)


def main(filename):
    with open(filename) as f:
        text = f.readlines()
    parser = Parser()
    parser.parse(text)

if __name__ == '__main__':
    import sys
    main(sys.args.file)
