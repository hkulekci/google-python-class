#!/usr/bin/python
# coding=UTF-8

import sys

def hello(name):
    if name == 'Alice' or name == 'Nick':
        print 'Alert: Alice and Nick Mode'
        name = name + '?????'
    else:
        print 'Others : ';
    name = name + '!!!!'
    print 'Hello', name

def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()