from database import database

def get_list():
    #sql = "SELECT name FROM countries ORDER BY name"
    #result = database.session.execute(sql)
    #return result.fetchall()
    list = ["Albania",
            "Australia",
            "Azerbaijan",
            "Belgia",
            "Bulgaria",
            "Espanja",
            "Georgia",
            "Irlanti",
            "Islanti",
            "Iso-Britannia",
            "Israel",
            "Italia",
            "Itävalta",
            "Kreikka",
            "Kroatia",
            "Kypros",
            "Latvia",
            "Liettua",
            "Malta",
            "Moldova",
            "Norja",
            "Pohjois-Makedonia",
            "Portugali",
            "Puola",
            "Ranska",
            "Romania",
            "Ruotsi",
            "Saksa",
            "San Marino",
            "Serbia",
            "Slovenia",
            "Suomi",
            "Sveitsi",
            "Tanska",
            "Tsekki",
            "Ukraina",
            "Venäjä",
            "Viro"]
    #result = database.session.execute(sql)
    #return result.fetchall()
    return list

def country_id(country):
    sql = "SELECT id FROM countries WHERE name =:country"
    result = database.session.execute(sql, {"country":country})
    id = result.fetchone()[0]
    return id


def country_name(id):
    sql = "SELECT name FROM countries WHERE id=:country_id"
    result = database.session.execute(sql, {"country_id":id})
    name = str(result.fetchone()[0])
    return name


def song_and_singer(country_id):
    sql = "SELECT singer, song FROM Songs_2021 WHERE country_id=:country_id"
    result = database.session.execute(sql, {"country_id":country_id})
    return result.fetchone()

