#!/usr/bin/python3
import MySQLdb

def list_states(username, password, db_name):
    db = MySQLdb.connect(host="localhost", port=3306, passwd="", db="hbtn_0e_0_usa")
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    
    for state in states:
        print(f"({state[0]}, '{state[1]}')")
    
    # Close the cursor and database connection
    cursor.close()
    db.close()