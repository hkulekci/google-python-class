#!/usr/bin/python
# coding=UTF-8

import sys

def hello(filename):
    f = open(filename, "rU")
    lines = f.readlines()
    print lines
    f.close()


def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()