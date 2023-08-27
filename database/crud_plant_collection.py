from database.database_connect import get_connector, DbConnectionError


def get_plant_in_collection_by_ids(user_id, plant_id):
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

def get_plants_data_in_user_collection(user_id):
	try:
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
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()

def get_user_collection(user_id):
	try:
		sql = f"SELECT * from plant_collection WHERE user_id = {user_id}"
		connector = get_connector()	
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

def add_plant_to_collection(plant_collection):
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
		raise DbConnectionError("Failed to add data to DB")
	finally:
		if connector:
			connector.close()
			
def update_plant_in_collection(plant_collection):
	try:
		sql = "UPDATE plant_collection SET last_care = %s, upcoming_care = %s WHERE user_id = %s AND plant_id = %s"
		val = (plant_collection['last_care'], plant_collection['upcoming_care'], plant_collection['user_id'], plant_collection['plant_id'])
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

def delete_plant_from_collection(user_id, plant_id):
	try:
		sql = "DELETE FROM plant_collection WHERE user_id = %s AND plant_id = %s"
		val = (user_id, plant_id)
		connector = get_connector()
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		cursor.close()
		return True
	except Exception:
		return False
	finally:
		if connector:
			connector.close()



