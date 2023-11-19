#!/usr/bin/python3
"""A module to fetch all states in states table"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    name = ''
    for char in argv[4].split()[0]:
        if char not in ('"\',;:'):
            name += char
    rows = session.query(State.id).filter_by(name=name)\
        .order_by(State.id).all()
    if rows:
        for row in rows:
            print(row.id)
    else:
        print("Not Found")
    # rows = session.query(State).get
    # for row in rows:
    #     if ('a' in row.name):
    #         print(f"{row.id}: {row.name}")
    session.close()
