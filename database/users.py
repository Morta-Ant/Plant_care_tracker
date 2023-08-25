import mysql.connector
from database.config import USER, PASSWORD, HOST, DATABASE
import bcrypt

#print(sys.path)

class DbConnectionError(Exception):
    pass
def _connect_to_db(DATABASE):
    cnx = mysql.connector.connect(  
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx



def get_all_records():
    try:
        db_name = DATABASE # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM users"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
#password='password123'
#hashed_passwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
record = {
    #'id':"",
    'firstname': 'Linda',
    'lastname': 'Smart',
    'email': 'Lsmart@gmail.com',
    'passwd': 'password123',
   
}
def get_user_by_email(email):
    db_name = DATABASE  # update as required
    db_connection = _connect_to_db(db_name)
    cur = db_connection.cursor(dictionary=True)
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cur.execute(query)
    row = cur.fetchone()
    for i in row:
            print(i)

    cur.close()


    return row



                
def insert_new_record(record):
    try:
        db_name = DATABASE
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        hashed_passwd = bcrypt.hashpw(record['passwd'].encode('utf-8'), bcrypt.gensalt())
        query = """INSERT INTO users ({}) VALUES (%s, %s, %s, %s)""".format(', '.join(record.keys()))
        values = (record['firstname'], record['lastname'], record['email'], hashed_passwd)
        cur.execute(query,values)
        #cur.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")
def get_plant_by_name(common_name):
    try:
        db_name = DATABASE # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print("Connected to DB: %s" % db_name)
        query = "SELECT * FROM plants WHERE common_name = %s"
        cur.execute(query, (common_name,))
        result = cur.fetchall()

        # query = """SELECT * FROM plants WHERE common_name={'Snake Plant'}"""
        # cur.execute(query)
        # result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
def get_all_records_plants():
    try:
        db_name = DATABASE # update as required
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(dictionary=True)
        print("Connected to DB: %s" % db_name)

        query = """SELECT common_name FROM plants"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")





def main():
    #get_all_records_plants()
    get_plant_by_name('Snake Plant')
    # get_all_records_for_rep('Morgan')
    #insert_new_record(record)
  
if __name__ == '__main__':
    main()