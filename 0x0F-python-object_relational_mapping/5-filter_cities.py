#!/usr/bin/python3
"""
A python module to print
states which their names
match user input from a database
"""


def main():
    import MySQLdb
    import sys
    argss = sys.argv[1:]
    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argss[0], passwd=argss[1], db=argss[2])
    name = ''
    for char in argss[3].split()[0]:
        if char not in ('"\',;:'):
            name += char
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                ON cities.state_id = states.id WHERE BINARY states.name = '{}'\
                ORDER BY cities.id ASC".format(name))
    rows = cur.fetchall()
    for row in range(len(rows)):
        print(rows[row][0], end=', ' if row != len(rows) - 1 else '')
    print()
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
