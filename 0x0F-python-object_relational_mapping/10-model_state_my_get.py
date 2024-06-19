#!/usr/bin/python3
"""A module to fetch all states that match user
input from states table (sql injection free)"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    row = session.query(State).filter(State.name == argv[4])\
        .order_by(State.id).all()
    if row:
        print(row[0].id)
    else:
        # there was an error in checks 5 and 8 because
        # I didn't copy the "Not found" instead I wrote it
        # like "Not 'f'ound" this caused an error!!!!!
        print("Not found")
    session.close()
