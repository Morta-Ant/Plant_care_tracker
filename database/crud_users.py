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

def get_all_users():
	connector = get_connector()
	try:
		sql = "SELECT * FROM users"
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
			
def get_user_by_id(id):
	try:
		sql = "SELECT * FROM users WHERE user_id = %s LIMIT 1"
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
			
def get_user_by_name(name):
  try:
    sql = "SELECT * FROM users WHERE LOWER(username) LIKE %s OR LOWER(email) LIKE %s"
    formattedText = f"%{name.lower()}%"
    val = (formattedText, formattedText)
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

def create_user(user):
	try:
		sql = "INSERT INTO users (username, email) VALUES (%s,%s)"
		val = (user['username'], user['email'])
		connector = get_connector()
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		user['user_id'] = cursor.lastrowid #This will get the latest Id added from the Insert, useful to return to the user
		cursor.close()
		return user
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()
			
def update_user(user):
	connector = get_connector()
	try:
		sql = "UPDATE users SET username = %s, email = %s WHERE user_id = %s"
		val = (user['username'], user['email'], user['user_id'])
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		cursor.close()
		return user
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()

def delete_user(id):
	connector = get_connector()
	cursor = connector.cursor()
	try:
		sql = "DELETE FROM users WHERE user_id = %s"
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


