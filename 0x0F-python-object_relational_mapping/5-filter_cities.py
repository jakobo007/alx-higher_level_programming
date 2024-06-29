#!/usr/bin/python3
"""script that lists all cities in a state"""
import MySQLdb
import sys


def list_cities(username, password, db_name, state_name):
    """Fucnction takes 4 args"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN state ON cities.state_id = states.id
    WHERE state.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    for city in cities:
        print(city)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        list_cities(username, password, db_name, state_name)