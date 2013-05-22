#!/usr/bin/python
# coding=UTF-8

import sys

def hello(filename):
    f = open(filename, "rU")
    text = f.read()

    words = {}
    
    for word in text.split():
        if word in words.keys():
            words[word] =  words[word] + 1
        else:
            words[word] = 1

    for key in words.keys():
        print key, " => ", words[key]

    f.close()


def main():
    hello(sys.argv[1])

if __name__ == "__main__": 
    main()