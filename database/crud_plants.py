from database.database_connect import get_connector, DbConnectionError


def get_all_plants():
	try:
		sql = "SELECT * FROM plants"
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

			
def get_plant_by_id(id):
	try:
		sql = "SELECT * FROM plants WHERE plant_id = %s LIMIT 1"
		val = (id, )
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


def get_plant_by_name(name):
  try:
    sql = "SELECT * FROM plants WHERE LOWER(common_name) LIKE %s OR LOWER(scientific_name) LIKE %s OR LOWER(other_name) LIKE %s"
    formattedText = f"%{name.lower()}%"
    val = (formattedText, formattedText, formattedText)
    connector = get_connector()
    cursor = connector.cursor(dictionary=True)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    cursor.close()
    return result
  except Exception:
    raise DbConnectionError("Failed to read data from DB")
  finally:
    if connector:
      connector.close()


def create_plant(plant):
	try:
		sql = "INSERT INTO plants (common_name, scientific_name, other_name, watering_frequency, growth_rate, light_level, maintenance_level, plant_description, image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val = (plant['common_name'], plant['scientific_name'], plant['other_name'], plant['watering_frequency'], plant['growth_rate'], plant['light_level'], plant['maintenance_level'], plant['plant_description'], plant['image'])
		connector = get_connector()
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		plant['plant_id'] = cursor.lastrowid #This will get the latest Id added from the Insert, useful to return to the user
		cursor.close()
		return plant
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()

def delete_plant(id):
	connector = get_connector()
	cursor = connector.cursor()
	try:
		sql = "DELETE FROM plants WHERE plant_id = %s"
		val = (id, )
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