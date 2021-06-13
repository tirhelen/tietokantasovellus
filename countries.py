from database import database

def get_list():
    sql = "SELECT name FROM countries ORDER BY name"
    result = database.session.execute(sql)
    return result.fetchall()

def song_and_singer(country_id):
    sql = "SELECT singer, song FROM Songs_2021 WHERE country_id=:country_id"
    result = database.session.execute(sql, {"country_id":country_id})
    return result.fetchone()
