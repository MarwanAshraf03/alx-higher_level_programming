#!/usr/bin/python3
"""A module that creates table states in hbtn_0e_6_usa"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """Creates table states in hbtn_0e_6_usa"""
    __tablename__ = "states"
    id = Column("id", Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)


# engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa',
#                        pool_pre_ping=True)
# Base.metadata.create_all(bind=engine)
