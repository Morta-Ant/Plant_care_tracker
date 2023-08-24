import mysql.connector
from database.config import HOST, USER, PASSWORD, DATABASE
from database.database_connect import get_connector, DbConnectionError
class DbConnectionError(Exception):
    pass

def get_connector(DATABASE):
	connector = mysql.connector.connect(
		host=HOST,
		user=USER,
		password=PASSWORD,
		auth_plugin='mysql_native_password',
		database=DATABASE
	)
	return connector



def get_all_plant_collections():
	db_name = DATABASE # update as required
	connector = get_connector(db_name)
	try:
		sql = """SELECT * FROM plant_collection"""
		cursor = connector.cursor(dictionary=True)
		cursor.execute(sql)
		result = cursor.fetchall()
		#cursor.close()
		#print(result)
		return result
	    #cursor.close(
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()


def get_plant_collection_by_ids(user_id, plant_id):
	db_name = DATABASE # update as required
	connector = get_connector(db_name)


	try:
		sql = "SELECT * FROM plant_collection WHERE user_id = %s AND plant_id = %s"
		val = (user_id, plant_id)
		#connector = get_connector()
		cursor = connector.cursor(dictionary=True)
		cursor.execute(sql, val)
		result = cursor.fetchone()
		
		print(result)
		cursor.close()
		return result
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()



			
			
def get_plant_collection_by_user(user_id):
	try:
		sql = "SELECT u.user_id,  u.username, u.email, (SELECT CONCAT('[', GROUP_CONCAT(JSON_OBJECT('common_name', p.common_name, 'upcoming_care', pc.upcoming_care)), ']') FROM plant_collection pc INNER JOIN plants p ON pc.plant_id = p.plant_id WHERE pc.user_id = u.user_id) AS plants FROM users u WHERE u.user_id = %s"
		val = (user_id, )
		connector = get_connector()
		cursor = connector.cursor(dictionary=True)
		cursor.execute(sql, val)
		result = cursor.fetchmany()
		cursor.close()
		return result
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()
plant_collection={
   'user_id':'2',
   'plant_id':'14',
   'last_care':'2023-07-29',
   'upcoming_care':'2020-09-27',

}
def get_plants_in_user_collection(user_id):
	sql = f"""SELECT pc.user_id, pc.plant_id, pc.upcoming_care, p.common_name, p.scientific_name, p.image FROM plant_collection pc
				LEFT JOIN plants p 
				ON p.plant_id = pc.plant_id
				WHERE user_id = {user_id}"""
	connector = get_connector()
	cursor = connector.cursor(dictionary=True)
	cursor.execute(sql)
	result = cursor.fetchall()
	cursor.close()
	return result

			


def add_plant_to_collection(plant_collection):
	try:
		db_name = DATABASE
		sql = "INSERT INTO plant_collection (user_id, plant_id, last_care, upcoming_care) VALUES (%s, %s, %s, %s)"
		val = (plant_collection['user_id'], plant_collection['plant_id'], plant_collection['last_care'], plant_collection['upcoming_care'])
		connector = get_connector(db_name)
		cursor = connector.cursor()
		print("Connected to DB: %s" % db_name)
		cursor.execute(sql, val)
		connector.commit()
		cursor.close()
		return plant_collection
	except Exception:
		raise DbConnectionError("Failed to add data to DB")
	finally:
		if connector:
			connector.close()





def update_plant_collection(plant_collection):

	connector = get_connector()
	try:
		sql = "UPDATE plant_collection SET last_care = %s, upcoming_care = %s WHERE user_id = %s AND plant_id = %s"
		val = (plant_collection['last_care'], plant_collection['upcoming_care'], plant_collection['user_id'], plant_collection['plant_id'])
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		cursor.close()
		return plant_collection
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()



def delete_plant_collection(user_id, plant_id):

	connector = get_connector()
	cursor = connector.cursor()
	try:
		sql = "DELETE FROM plant_collection WHERE user_id = %s AND plant_id = %s"
		val = (user_id, plant_id)
		cursor.execute(sql, val)
		connector.commit()
		cursor.close()
		return True
	except Exception:
		return False
	finally:
		if cursor:
			cursor.close()
		if connector:
			connector.close()
def create_plant_collection(plants_rec):
    try:
        db_name = DATABASE
        db_connection = get_connector(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query = """INSERT INTO plant_collection ({}) VALUES (%s, %s, %s, %s)""".format(', '.join(plants_rec.keys()))
        values = (plants_rec['user_id'],plants_rec['plant_id'], plants_rec['last_care'],plants_rec['upcoming_care'])
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
	#create_plant_collection(plant_collection)
    #get_all_plant_collections()
	get_plant_collection_by_ids(1,2)
if __name__ == '__main__':
    main()

