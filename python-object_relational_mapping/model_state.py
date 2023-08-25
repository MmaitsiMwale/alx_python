#!/usr/bin/python3

"""python file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config import DATABASE_CONFIG


Base = declarative_base()


class State(Base):
    """represents an instant of the table states
        id: primary key for states table
        name : name of state
    """

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)  # primary key
    name = Column("name", String(length=128))  # column for state names
