#!/usr/bin/python3
"""Imported modules"""
import MySQLdb
import sys


def list_states(username, password, db_name, search_item):
    """takes an item and displays all values"""

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(search_item)
    cursor.execute(query)
    states = cursor.fetchall()
    
    for state in states:
        print(f"({state[0]}, '{state[1]}')")

    cursor.close()
    db.close()

if __name__ == "__main__":
    
    if len(sys.argv) == 5:
        username = argv[1]
        password = argv[2]
        db_name = argv[3]
        search_item = argv[4]
        list_states(username, password, db_name, search_item)