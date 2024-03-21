#!/usr/bin/python3
"""
adds the State object “Louisiana”
"""
from os import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_state = session.query(State).filter_by(name='Louisiana').first()
    print(new_state.id)
    session.commit()
