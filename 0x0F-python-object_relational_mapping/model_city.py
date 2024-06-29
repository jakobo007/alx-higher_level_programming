#!/usr/bin/pyton3
"""Imported modules"""
from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from model_state import Base

class City(Base):
    """Class definition"""
    __tablename__ = 'cities'
    id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    