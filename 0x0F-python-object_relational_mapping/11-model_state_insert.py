#!/usr/bin/python3
"""A module to add Louisiana state in states table"""
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
    newState = State(name="Louisiana")
    session.add(newState)
    addedState = session.query(State).filter(State.name == "Louisiana").all()
    print(addedState[0].id)
    session.commit()
    session.close()
