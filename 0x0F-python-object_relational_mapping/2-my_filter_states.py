#!/usr/bin/python3
"""
List all states starting with N
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        username=argv[1],
        password=argv[2],
        database=argv[3],
        host='localhost',
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE
                BINARY '{}'".format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
