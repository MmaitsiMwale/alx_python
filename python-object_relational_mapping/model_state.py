from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

"""python file that contains the class definition of a
State and an instance Base = declarative_base()"""

Base = declarative_base()


class State(Base):
    """State represents an instant of the table states
        :id: primary key for states table
        :name: name of state
    """

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column("name", String(length=128))
