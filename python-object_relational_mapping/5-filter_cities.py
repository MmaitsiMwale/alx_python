#!/usr/bin/python3

"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database"""


from MySQLdb import connect
import sys


def list_all_states(username, password, database_name, state_name):
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

    # Create a query to get all cities from the table cities:
    select_query = """SELECT cities.name
    FROM `cities` JOIN `states` on cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id """
    cursor.execute(select_query, (state_name,))
    query_rows = cursor.fetchall()
    cities = ", ".join(city[0] for city in query_rows)
    print(cities, end="")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 5
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        list_all_states(username, password, database_name, state_name)
    except AssertionError:
        print(
            f"Usage : ./{__file__} username password databasename state_name")
