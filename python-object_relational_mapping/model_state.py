#!/usr/bin/python3

"""python file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_CONFIG
import datetime as dt


Base = declarative_base()


class State(Base):
    """represents an instant of the table states"""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)  # primary key
    name = Column("name", String(length=128))  # column for state names
