#!/usr/bin/python3
"""Imported Modules"""
import MySQLdb
import sys


def list_cities(username, password, db_name):
    """List all cities in hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            )    
sffjf

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_cities(username, password, db_name)
