#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_all_state_obj(username, password, database):
    """lists all state object in db in ascending order"""
    db = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by('id').all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4
        list_all_state_obj(sys.argv[1], sys.argv[2], sys.argv[3])
    except AssertionError:
        "Please provide three arguments after the program name"
