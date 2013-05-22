#!/usr/bin/python
# coding=UTF-8


#This code work with
#    $ python test.0.2.py Alice
#
#but Except an error with
#    $ python test.0.2.py mark 


import sys

def hello(name):
    if name == 'Alice' or name == 'Nick':
        print 'Alert: Alice and Nick Mode'
        name = name + '?????'
    else:
        DoesNotExist()
    name = name + '!!!!'
    print 'Hello', name

def main():
    hello(sys.argv[1])

if __name__ == "__main__":
    main()