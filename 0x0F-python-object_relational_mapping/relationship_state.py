#!/usr/bin/python3
"""A module that creates table states in hbtn_0e_6_usa"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
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
    cities = relationship('City', backref='states', cascade='all, delete')
