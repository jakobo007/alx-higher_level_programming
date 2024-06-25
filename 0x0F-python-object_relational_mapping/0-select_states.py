#!/usr/bin/python3
"""Imported modules"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """Lists all states from hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    
    cursor = db.cursor()
    cursor.execute("""
                   SELECT id, name
                   FROM states
                   ORDER BY id ASC""")
    
    states = cursor.fetchall()
    
    for state in states:
        print(f"({state[0]}, '{state[1]}')")
    
    cursor.close()
    db.close()
    
    
    
if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(username, password, db_name)
