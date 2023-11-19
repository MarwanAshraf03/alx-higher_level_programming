#!/usr/bin/python3
"""A python module to print
states which their names
match user input from a database"""


def main():
    import MySQLdb
    import sys
    argss = sys.argv[1:]
    db = MySQLdb.Connect(
        host="localhost", user=argss[0], passwd=argss[1], db=argss[2])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE\
    name like '{}' ORDER BY states.id ASC".format(argss[3])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main()
