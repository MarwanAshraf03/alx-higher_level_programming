#!/usr/bin/python3
"""A module that creates table cities in hbtn_0e_6_usa"""
from sqlalchemy import ForeignKey, Column, String, Integer
from model_state import Base


class City(Base):
    """Creates table cities in hbtn_0e_6_usa"""
    __tablename__ = "cities"
    id = Column("id", Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id",
                      Integer,
                      ForeignKey("states.id"),
                      nullable=False)
