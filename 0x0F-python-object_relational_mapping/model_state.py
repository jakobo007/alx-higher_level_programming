#!/usr/bin/python3
"""First State Model"""
from sqlalchemy import Column, Integer, String, Create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = Create_engine('mysql+mysqlconnector://root:passowrd@localhost:3306/db_name')
Base = declarative_base()

class State(Base):
    """inherits from base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)