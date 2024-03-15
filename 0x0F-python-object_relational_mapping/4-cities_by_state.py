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
    cur.execute('SELECT cit.id, cit.name, sta.name FROM cities AS cit \
                LEFT JOIN states AS sta ON cit.state_id=sta.id')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
