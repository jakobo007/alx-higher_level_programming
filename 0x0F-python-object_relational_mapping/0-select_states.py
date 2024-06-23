#!/usr/bin/python3
#!/usr/bin/env python3
import sys
import MySQLdb

def list_states(username, password, db_name):
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    
    # Execute the query to select all states sorted by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    
    # Fetch all the results
    states = cursor.fetchall()
    
    # Print the results
    for state in states:
        print(state)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(username, password, db_name)
    else:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
