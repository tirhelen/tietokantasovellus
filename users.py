from flask import session
from database import database
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):

	sql = "SELECT password, id FROM Users WHERE username=:username"
	result = database.session.execute(sql, {"username":username})
	user = result.fetchone()

	if user == None:
		return False

	else:
		if check_password_hash(user[0], password):
			session["user_id"] = user[1]
			return True
		else:
			return False


def logout():
	del session["user_id"]


def register(username, password):
	hash = generate_password_hash(password)

	try:
		sql = "INSERT INTO Users (username, password) VALUES (:username,:password)"
		database.session.execute(sql, {"username":username, "password":hash})
		database.session.commit()
	except:
		return False
		
	return login(username, password)
 