#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id""", (sys.argv[4],))
    list_cities = cur.fetchall()
    list_str = []
    for city in list_cities:
        list_str.append(city[0])
    city_str = ', '.join(list_str)
    print(city_str)
    db.close()
