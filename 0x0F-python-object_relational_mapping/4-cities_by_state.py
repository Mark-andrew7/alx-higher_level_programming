#!/usr/bin/python3
"""
lists all cities
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host='localhost',
        port=3306
    )

    cur = db.cursor()
    cur.execute('SELECT * FROM cities ORDER BY id ASC')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
