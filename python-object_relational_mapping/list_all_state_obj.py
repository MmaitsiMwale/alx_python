from model_state import Base, State


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_state_obj(username, password, database):
    """lists all state object in db"""
    db = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by('name').all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
