#!/usr/bin/python3
"""List all State objects from hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    """Create a Session class"""
    Session = sessionmaker(bind=engine)
    
    """create a session"""
    session = Session()
    
    """Query the database"""
    states = session.query(State).filter(State.name.ilike('%a%')).all()
    
    """query database, delete states and commit changes"""
    for state in states:
        session.delete(state)
    session.commit()

    session.close()