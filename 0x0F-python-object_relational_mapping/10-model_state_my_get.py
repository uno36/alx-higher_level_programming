#!/usr/bin/python3
"""  a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter(
        State.name == sys.argv[4]).first()
    if state_id is None:
        print("Not found")
    else:
        print("{:d}".format(state_id.id))
