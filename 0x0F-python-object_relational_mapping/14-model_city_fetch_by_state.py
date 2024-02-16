#!/usr/bin/python3
"""A module to print cities, states, and cities' ids"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
