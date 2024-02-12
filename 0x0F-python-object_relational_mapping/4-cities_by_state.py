#!/usr/bin/python3
"""
A python module to print
cities ids, cities names, and states names
"""


def main():
    import MySQLdb
    import sys
    argss = sys.argv[1:]
    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argss[0], passwd=argss[1], db=argss[2])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
