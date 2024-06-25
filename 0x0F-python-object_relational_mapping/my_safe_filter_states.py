#!/usr/bin/python3
"""Imported modules"""
import MySQLdb
import sys


def list_states(username, password, db_name, search_item):
    """takes an item and displays all values"""

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    cursor = db.cursor()
    query = """
    SELECT *
    FROM states
    WHERE name = '' %s
    ORDER BY id ASC"""
    cursor.execute(query, (search_item,))
    states = cursor.fetchall()
    
    for state in states:
        print(f"({state[0]}, '{state[1]}')")

    cursor.close()
    db.close()

if __name__ == "__main__":
    
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        search_item = sys.argv[4]
        list_states(username, password, db_name, search_item)
