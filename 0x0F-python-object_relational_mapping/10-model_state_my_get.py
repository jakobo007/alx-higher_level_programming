#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state_name = sys.argv[4]
    
    """Create a Session class"""
    Session = sessionmaker(bind=engine)
    
    """create a session"""
    session = Session()
    
    """Query the database and sort the results by state.id"""
    state = session.query(State).filter(State.name == state_name).first()
    
    if state:
        print(f"{state.id}")
    else:
        print("Not Found")

    session.close()