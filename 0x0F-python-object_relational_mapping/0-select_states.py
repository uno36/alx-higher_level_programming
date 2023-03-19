#!/usr/bin/python3
""" a script that lists all states from
the database hbtn_0e_0_usa """
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
    cur.execute("SELECT * FROM states")
    list_states = cur.fetchall()
    for state in list_states:
        print("{}".format(state))
    db.close()
