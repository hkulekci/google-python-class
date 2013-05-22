#!/usr/bin/python
# coding=UTF-8


#This code work with
#    $ python test.0.2.py Alice
#
#but Except an error with
#    $ python test.0.2.py mark 


import sys

def str(name):
    # String convert to list
    chars = []
    for character in name:
        chars.append(character)
        print character
    
    # not copied, memory is linked.
    b = chars
    b[2] = 's'
    # copied to c
    c = chars[:]
    c[2] = 'y'

    print "Second Character : ", chars[2]
    print "list of chars"
    for character in chars:
        print character
    
    print "list of chars"
    for character in chars:
        print character

    print "list of c"
    for character in c:
        print character

    print "`'y' in c` is ", 'y' in c
    

def main():
    str(sys.argv[1])

if __name__ == "__main__":
    main()