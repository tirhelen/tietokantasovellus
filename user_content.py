from database import database
import users

def send_message(message, country_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO comments (user_id, song_id, message, sent) VALUES (:user_id, :song_id, :message, NOW())"
    database.session.execute(sql, {"user_id":user_id, "song_id":country_id, "message":message})
    database.session.commit()
    return True

def get_messages(country_id):
    sql = "SELECT C.message, U.username, C.sent FROM comments C, users U WHERE C.user_id=U.id AND C.song_id=:country_id"
    result = database.session.execute(sql, {"country_id":country_id})
    return result.fetchall()

def get_points(country_id):
    user_id = users.user_id()
    if user_id == 0:
        return None
    sql = "SELECT points FROM points WHERE user_id=:user_id AND song_id=:country_id"
    result = database.session.execute(sql, {"user_id":user_id, "country_id":country_id})
    return result.fetchone()
