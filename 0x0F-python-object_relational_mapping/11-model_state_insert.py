#!/usr/bin/python3
"""Adds a new state to database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    """Create a Session class"""
    Session = sessionmaker(bind=engine)
    
    """create session"""
    session = Session()
    """Create new state obj to add"""
    new_state = State(name="Louisiana")
    
    """Add to session and commit to db"""
    session.add(new_state)
    session.commit()
    
    """print results"""
    print(new_state.id)
    
    """Close session"""
    session.close()