#!/usr/bin/python3
"""
changes the name of a State object
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'
    session.commit()
