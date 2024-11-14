# db_connect.py

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # e.g., 'localhost'
        user='root',
        password='',
        database='petid'
    )
    return connection
