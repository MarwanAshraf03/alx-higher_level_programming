#!/usr/bin/python3
"""A module to update state with id 2 to New Mexico in states table"""
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
    modState = session.query(State).filter(State.id == 2).all()
    modState[0].name = 'New Mexico'
    session.commit()
    session.close()
