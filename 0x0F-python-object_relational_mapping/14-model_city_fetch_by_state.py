#!/usr/bin/python3
""" a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for query in session.query(State, City).filter(
            State.id == City.state_id):
        print("{:s}: ({:d}) {:s}".format(
            query.State.name, query.City.id, query.City.name))
