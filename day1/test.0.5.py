#!/usr/bin/python
# coding=UTF-8

import sys

def hello(filename):
    f = open(filename, "rU")
    for line in f:
        print line, # if you remove the comma from this line, \n is written by print function. You can try now, remove comma.
    f.close()


def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()