#!/usr/bin/python3
"""
MySQLdb module used
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
       username=argv[1],
       password=argv[2],
       database=argv[3]),
       host='localhost',
       port=3306

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()
