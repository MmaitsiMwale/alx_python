#!/usr/bin/python3

"""Script that lists all states that the user passes from the
database hbtn_0e_0_usa"""


from MySQLdb import connect
import sys


def list_all_states(username, password, database_name, argument):
    """
    lists all states in the table states from the database hbtn_0e_0_usa
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

    # Create a query to get all states from the table states:
    select_query = "SELECT * FROM `states` WHERE name LIKE BINARY %s"
    cursor.execute(select_query, (argument,))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 5
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        argument = sys.argv[4]
        list_all_states(username, password, database_name, argument)
    except AssertionError:
        print(f"Usage : ./{__name__} username password databasename argument")
