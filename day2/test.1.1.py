#!/usr/bin/python
# coding=UTF-8

"""
Find the email adress from the file content
"""

import re
import sys

def hello(filename):
    f = open(filename, "rU")
    text = f.read()

    match1 = re.search(r'\w[\w.]*@[\w.]+', text);
    if match1:
        print "Email Adress : ", match1.group()
    else:
        print 'Not found!';

    match2 = re.search(r'([\w.]+)@([\w.]+)', text);
    if match2: 
        print "Email Adress : ", match2.group()
        print "Parts of the mail : "
        print "Part 0 : ", match2.group(0)
        print "Part 1 : ", match2.group(1) # for parantesis 1 not for brackets
        print "Part 2 : ", match2.group(2) # for parantesis 2 not for brackets
    else:
        print 'Not found!';

    f.close()


def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()