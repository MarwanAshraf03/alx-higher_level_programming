#!/usr/bin/python3
"""A python module to print
states which has N as a first letter in
their name from a database"""


def main():
    import MySQLdb
    import sys
    argss = sys.argv[1:]

    db = MySQLdb.Connect(
        host="localhost", user=argss[0], passwd=argss[1], db=argss[2])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main()
