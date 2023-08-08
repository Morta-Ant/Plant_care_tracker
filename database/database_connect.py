import mysql.connector
from database.config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    # Code to connect to a mysql database, uses the auth details
    # in config.py
    connectDB = mysql.connector.connect(
        User=USER,
        password=PASSWORD,
        host=HOST,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return connectDB