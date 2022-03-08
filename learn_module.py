#!usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'  # docstring for this module

__author__ = 'Anqi Wu'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hi!')
    elif len(args) == 2:
        print(f"Hi {args[1]}!")
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
