from flask import session
from database import database
from werkzeug.security import check_password_hash, generate_password_hash

def login(kayttajanimi, salasana):
	sql = "SELECT salasana, id FROM Kayttajat WHERE kayttajanimi=:kayttajanimi"
	tulos = database.session.execute(sql, {"kayttajanimi":kayttajanimi})
	kayttaja = tulos.fetchone()
	if kayttaja == None:
		return False
	else:
		if check_password_hash(kayttaja[0], salasana):
			session["kayttaja_id"] = kayttaja[1]
			return True
		else:
			return False

def logout():
	del session["kayttaja_id"]


def register(kayttajanimi, salasana):
	hash = generate_password_hash(salasana)
	try:
		sql = "INSERT INTO Kayttajat (kayttajanimi, salasana) VALUES (:kayttajanimi,:salasana)"
		database.execute(sql, {"kayttajanimi":kayttajanimi, "salasana":hash})
		database.session.commit()
	except:
		return False
	return login(kayttajanimi, salasana)
 
