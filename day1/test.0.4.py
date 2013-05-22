#!/usr/bin/python
# coding=UTF-8

import sys

def hello():
    # list example 
    a = ['a', 'b', 1, 'c']
    a[0] = 2
    print sorted(a)

    # Tuple Example
    b = (1,'b',3,'a',5)
    # Tuple is inmutable
    # b[0] = 2 # this line gives an error
    print sorted(b)

    # Hashtable Example
    d = {}
    d['a'] = 'alpha'
    d['b'] = 'beta'
    d['g'] = 'gama'
    print d
    print d.keys()
    print d.values()
    for k in sorted(d.keys()):
        print "key: ", k, '->', d[k]

    print d.items()

def main():
    hello()

if __name__ == "__main__": 
    main()