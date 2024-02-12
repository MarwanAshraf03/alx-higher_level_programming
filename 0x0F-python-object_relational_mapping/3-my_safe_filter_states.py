#!/usr/bin/python3
"""A python module to print
states which their names
match user input from a database sql injection free"""


def main():
    import MySQLdb
    import sys
    argss = sys.argv[1:]
    db = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=argss[0], passwd=argss[1], db=argss[2])
    cur = db.cursor()
    """The Binary keyword is used to provide case-sensitive comparison"""
    name = ''
    for char in argss[3].split()[0]:
        if char not in ('"\',;:'):
            name += char
    query = """SELECT * FROM states WHERE
    BINARY name = '{}' ORDER BY states.id ASC""".format(name)
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
