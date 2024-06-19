#!/usr/bin/python3
"""A module to print cities, states, and cities' ids"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    n_state = State(name='California')

    session.add(n_state)
    session.commit()
    n_city = City(name='San Francisco', state_id=n_state.id)
    session.add(n_city)
    session.commit()
    session.close()
