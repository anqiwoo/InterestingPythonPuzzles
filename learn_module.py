#!usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'  # docstring for this module

__author__ = 'Anqi Wu'

import sys
import os


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hi!')
    elif len(args) == 2:
        print(f"Hi {args[1]}!")
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    # test()
    print(os.path.split(__file__)[1])
    print(os.path.split(os.path.split(__file__)[0]))
    for path, dirs, files in os.walk(__file__, topdown=True):
        for _dir in dirs:
            print(os.path.join(path, _dir))
        for _file in files:
            print(os.path.join(path, _file))
