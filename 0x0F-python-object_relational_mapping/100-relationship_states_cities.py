#!/usr/bin/python3
"""A module to print cities, states, and cities' ids"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    # from model_state import Base, State
    # from model_city import City
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    n_state = State(name='California')
    n_city = City(name='San Francisco')

    session.add(n_state)
    session.add(n_city)
    session.close()
