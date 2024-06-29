#!/usr/bin/python3
"""Imported modules"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    """creat session class"""
    Session = sessionmaker(bind=engine)
    
    """Start session"""
    session = Session()
    
    """query the database and print results"""
    cities = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    
    session.close()
