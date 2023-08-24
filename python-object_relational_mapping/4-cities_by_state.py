#!/usr/bin/python3

"""Script that lists all cities fro the database hbtn_0e_0_usa"""


from MySQLdb import connect
import sys


def list_all_cities(username, password, database_name):
    """
    lists all cities in the table cities from the database hbtn_0e_0_usa
    """
    # get connection details
    conn = connect(
        user=username,
        passwd=password,
        db=database_name,
        host="localhost",
        port=3306,
    )

    cursor = conn.cursor()

    # Create a query to get all cities from the table cities:
    select_query = "SELECT * FROM `cities` ORDER BY id"
    cursor.execute(select_query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_all_cities(username, password, database_name)
    except AssertionError:
        print(f"Usage : ./{__name__} username password databasename")
