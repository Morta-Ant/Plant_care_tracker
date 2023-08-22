import mysql.connector
from database.config import HOST, USER, PASSWORD, DATABASE

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


def get_all_plants():
	connector = get_connector(DATABASE)
	try:
		sql = "SELECT * FROM plants"
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
			
# def get_plant_by_name(name,connector):
#   try:
#     sql = "SELECT * FROM plants WHERE LOWER(common_name) LIKE %s OR LOWER(scientific_name) LIKE %s OR LOWER(other_name) LIKE %s"
#     formattedText = f"%{name.lower()}%"
#     val = (formattedText, formattedText, formattedText)
#     connector = get_connector(DATABASE)
#     cursor = connector.cursor(dictionary=True)
#     cursor.execute(sql, val)
#     result = cursor.fetchall()
#     cursor.close()
#     return result
#   except Exception:
#     raise DbConnectionError("Failed to read data from DB")
#   finally:
#     if connector:
#       connector.close()
      
	
	  
    #How do i pint the results to the terminal 
      


			
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
			
def update_plants(plant):
	connector = get_connector()
	try:
		sql = "UPDATE plants SET common_name = %s, scientific_name = %s, other_name = %s, watering_frequency = %s, growth_rate = %s, light_level = %s, maintenance_level = %s, plant_description = %s, image = %s  WHERE plant_id = %s"
		val = (plant['common_name'], plant['scientific_name'], plant['other_name'], plant['watering_frequency'], plant['growth_rate'], plant['light_level'], plant['maintenance_level'], plant['plant_description'], plant['image'], plant['plant_id'])
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
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

def get_plant_by_name(common_name):
    try:
        db_name = DATABASE # update as required
        db_connection = get_connector(db_name)
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
        db_connection = get_connector(db_name)
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
   get_plant_by_name('Snake Plant') 
   get_plant_by_id(1) 				
if __name__ == '__main__':
    main()
 