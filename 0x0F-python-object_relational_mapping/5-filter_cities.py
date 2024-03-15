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
    cur.execute('SELECT cit.name FROM cities AS cit \
                JOIN states AS sta \
                ON cit.state_id = sta.id \
                WHERE sta.name = %s \
                ORDER by cit.id ASC', (argv[4],))

    rows = cur.fetchall()
    cities = ''
    for row in rows:
        cities += row[0] + ','

    if(cities):
        print(cities)

    cur.close()
    db.close()
