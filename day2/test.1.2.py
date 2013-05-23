#!/usr/bin/python
# coding=UTF-8

"""
Find all the email adress from the file content
"""

import re
import sys

def hello(filename):
    f = open(filename, "rU")
    text = f.read()

    match1 = re.findall(r'\w[\w.]*@[\w.]+', text);
    if match1:
        print "Email Adresses : "
        print match1
    else:
        print 'Not found!';

    match2 = re.findall(r'([\w.]+)@([\w.]+)', text);
    if match2: 
        print "Email Adresses with parantesis : "
        print match2
    else:
        print 'Not found!';

    match3 = re.findall(r'([\w.]+)@([\w.]+)', text, re.IGNORECASE);
    if match3: 
        print "Email Adresses with parantesis : "
        print match3
    else:
        print 'Not found!';

    """
    Some research is necessery for re.IGNORECASE, re.DOTALL, ... etc.
    """

    f.close()


def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()