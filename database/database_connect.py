import mysql.connector
from config import USER, PASSWORD, HOST
dbname='plantregister'

class DbConnectionError(Exception):
    pass

def _connect_to_db(dbname):
    # Code to connect to a mysql database, uses the auth details
    # in config.py
    connectDB = mysql.connector.connect(
        User=USER,
        password=PASSWORD,
        host=HOST,
        auth_plugin='mysql_native_password',
        database=dbname
    )
    return connectDB