#!/usr/bin/python3
"""A module to fetch all states in states table"""
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1],
    argv[2],
    argv[3]),
    pool_pre_ping=True)

Session = sessionmaker(engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
