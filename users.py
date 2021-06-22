from flask import session
from database import database
from werkzeug.security import check_password_hash, generate_password_hash
from secrets import token_hex


def login(username, password):

	sql = "SELECT password, id, is_admin FROM Users WHERE username=:username"
	result = database.session.execute(sql, {"username":username})
	user = result.fetchone()
	if user == None:
		return False

	else:
		if check_password_hash(user[0], password):
			session["is_admin"] = user[2]
			session["user_id"] = user[1]
			session["csrf_token"] = token_hex(16)
			return True
		else:
			return False


def logout():
	del session["is_admin"]
	del session["csrf_token"]
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


def user_id():
	return session.get("user_id", 0)


def is_username_available(username):
	sql = "SELECT id FROM Users WHERE username=:username"
	result = database.session.execute(sql, {"username":username})
	id = result.fetchone()
	if id is not None:
		return False
	else:
		return True


def is_admin(id):
	sql = "SELECT is_admin FROM Users WHERE id=:id"
	result = database.session.execute(sql, {"id":id})
	admin = result.fetchone()
	if not admin[0]:
		return False
	else:
		return True
