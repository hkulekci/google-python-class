#!/usr/bin/python
# coding=UTF-8

"""
Find first match example. Finding only one mathing.

Some usage :

Search for "Lorem"
Exactly Pattern : "Lorem"
 $ python test.1.0.py alice.txt Lorem

Search For "...em" => three character and "em"
Exactly Pattern : "...em"
 $ python test.1.0.py alice.txt ...em

Search for "est."
Exactly Pattern : "est\."
 $ python test.1.0.py alice.txt est\\. 

Search for ":\w\w\w" three character after semicolon.
Exactly Pattern : ":\w\w\w"
 $ python test.1.0.py alice.txt :\\w\\w\\w.

Search for "rem" characters ended with a blank character
Exactly Pattern : "rem\s"
 $ python test.1.0.py alice.txt rem\\s.

Search for three digit number
Exactly Pattern : "\d\d\d"
 $ python test.1.0.py long-alice.txt \\d\\d\\d

Search for one or more digit number
Exactly Pattern : "\d+"
 $ python test.1.0.py long-alice.txt \\d+

Search for starting with "Lor" and ended with blank character word
Exactly Pattern : "Lor\w+\s"
 $ python test.1.0.py long-alice.txt Lor\\w+\\s


.(dot)  any character
\w      word character
\d      digit
\s      whitespace (blank) character
\S      non-whitespace character
+       1 or more
*       0 or more 


"""

import re
import sys

def hello(filename, pattern):
    f = open(filename, "rU")
    text = f.read()
    match = re.search(pattern, text);
    if match: 
        print match.group()
    else:
        print 'Not found!';

    f.close()


def main():
    hello(sys.argv[1], sys.argv[2])

if __name__ == "__main__": 
    main()