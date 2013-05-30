#!/usr/bin/python
import MySQLdb

"""
If you use ubuntu firstly, you should run the following line:
    $ apt-get install python-MySQLdb
Otherwise, you can execute the following line:
    $ pip install MySQLdb 
"""

# connection
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="test")
cursor = db.cursor()

cursor.execute("SELECT * FROM test_table") 

numrows = int(cursor.rowcount)

for x in range(0, numrows):
    row = cursor.fetchone()
    print row[0], " ", row[1]


