import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

class DbConnectionError(Exception):
    pass

def get_connector():
	connector = mysql.connector.connect(
		host=HOST,
		user=USER,
		password=PASSWORD,
		database=DATABASE
	)
	return connector


def get_all_plant_collections():
	connector = get_connector()
	try:
		sql = "SELECT * FROM plant_collection"
		cursor = connector.cursor(dictionary=True)
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		return result
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()

def get_plant_collection_by_ids(user_id, plant_id):
	try:
		sql = "SELECT * FROM plant_collection WHERE user_id = %s AND plant_id = %s"
		val = (user_id, plant_id)
		connector = get_connector()
		cursor = connector.cursor(dictionary=True)
		cursor.execute(sql, val)
		result = cursor.fetchone()
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

def create_plant_collection(plant_collection):
	try:
		sql = "INSERT INTO plant_collection (user_id, plant_id, last_care, upcoming_care) VALUES (%s, %s, %s, %s)"
		val = (plant_collection['user_id'], plant_collection['plant_id'], plant_collection['last_care'], plant_collection['upcoming_care'])
		connector = get_connector()
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
