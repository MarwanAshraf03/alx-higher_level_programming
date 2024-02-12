#!/usr/bin/python3
"""A module to fetch all states in states table (using sqlalchemy)"""
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
    for row in session.query(State).order_by(State.id).all():
        print(f"{row.id}: {row.name}")
    session.close()
