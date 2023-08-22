import bcrypt
from database.config import DATABASE
from database.database_connect import get_connector, DbConnectionError

def get_all_records():
    try:
        db_name = DATABASE  # update as required
        db_connection = get_connector()
        cur = db_connection.cursor()
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
    db_name = DATABASE
    db_connection = get_connector()
    cur = db_connection.cursor()
    print("Connected to DB: %s" % db_name)
    query = f"SELECT * FROM users WHERE email = {'email'}"
    cur.execute(query)
    row = cur.fetchone()
    return row


def insert_new_record(record):
    try:
        db_name = DATABASE
        db_connection = get_connector()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        hashed_passwd = bcrypt.hashpw(record['passwd'].encode('utf-8'), bcrypt.gensalt())
        query = """INSERT INTO users ({}) VALUES (%s, %s, %s, %s)""".format(', '.join(record.keys()))
        values = (record['firstname'], record['lastname'], record['email'], hashed_passwd)

        #query = """INSERT INTO users ({}) VALUES ('{}', '{}', '{}', '{}')""".format(
         #   ', '.join(record.keys()),
            #record['id'],
          #  record['firstname'],
           # record['lastname'],
           # record['email'],
           # #hashed_passwd,
          #  record['passwd'],
       # )
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

def main():
    get_all_records()
    # get_all_records_for_rep('Morgan')
    #insert_new_record(record)


if __name__ == '__main__':
    main()


