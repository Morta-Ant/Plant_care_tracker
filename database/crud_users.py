import bcrypt
from database.database_connect import get_connector, DbConnectionError

      
def get_user_by_email(email):
  try:
    sql = "SELECT * FROM users WHERE LOWER(email) LIKE %s"
    formattedText = f"%{email.lower()}%"
    val = (formattedText, )
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

def create_user(user):
	try:
		hashed_passwd = bcrypt.hashpw(user['passwd'].encode('utf-8'), bcrypt.gensalt())
		sql = "INSERT INTO users (firstname, lastname, email, passwd) VALUES (%s,%s,%s,%s)"
		val = (user['firstname'], user['lastname'], user['email'], hashed_passwd)
		connector = get_connector()
		cursor = connector.cursor()
		cursor.execute(sql, val)
		connector.commit()
		user['user_id'] = cursor.lastrowid #This will get the latest Id added from the Insert, useful to return to the user id
		cursor.close()
		return user
	except Exception:
		raise DbConnectionError("Failed to read data from DB")
	finally:
		if connector:
			connector.close()
			
def get_user_emails():
	connector = get_connector()
	cursor = connector.cursor()
	try:
		sql = "SELECT email FROM users"
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		result = [t[0] for t in result] #unpacking tuple to get a list of emails
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