import mysql.connector
from colors import *
# DATABASE CONNECTION
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database="flight_game",
            autocommit=True
        )
        print(f'{color_red}Connected to database Air Travellers Challenge{color_end}')
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# SQL QUERY FUNCTIONS
def execute_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    try:
        if len(params) > 1:
            cursor.execute(query, params)
        elif params:
            cursor.execute(query, (params,))
        else:
            cursor.execute(query)
        connection.commit()
        return cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

# Function to fetch data from the database
def fetch_data(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    try:
        if type(params) == int:
            cursor.execute(query, (params, ))
        elif params is not None and len(params) > 2:
            cursor.execute(query, params)
        elif params:
            cursor.execute(query, (params,))
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

def fetch_one(connection, query, params=None):
    cursor = connection.cursor()

    try:
        if params:
            cursor.execute(query, (params,))
        else:
            cursor.execute(query)

        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

def fetch_coords(connection, query, lat, lon):
    cursor = connection.cursor()

    try:
        if lat:
            cursor.execute(query, (lat, lon))
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()




