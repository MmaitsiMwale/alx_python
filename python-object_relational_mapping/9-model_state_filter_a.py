#!/usr/bin/python3
""" a script that lists all state objects that have 'a'from the database
hbtn_0e_6_usa"""
from model_state import Base, State


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_state_with_a(username, password, database):
    """lists all state object in db in ascending order"""
    db = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(
        State.id).filter(State.name.ilike(f"%a%")).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4
        list_state_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
    except AssertionError:
        "Please provide three arguments after the program name"
