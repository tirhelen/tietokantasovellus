from database import database
import users
from flask import session


def send_message(message, country_id):

    user_id = users.user_id()
    if user_id == 0:
        return False
    if 0 < len(message) < 5000:
        # checking if user is trying to send the same message again
        sql = "SELECT id FROM comments WHERE user_id=:user_id AND message=:message AND song_id=:song_id"
        result = database.session.execute(sql, {"user_id":user_id, "message":message, "song_id":country_id})
        id = result.fetchone()
        if id is not None:
            return False
        else:
            sql = "INSERT INTO comments (user_id, song_id, message, sent) VALUES (:user_id, :song_id, :message, NOW())"
            database.session.execute(sql, {"user_id":user_id, "song_id":country_id, "message":message})
            database.session.commit()
            return True
    else:
        return False


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


def add_points(points, country_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        points = int(points)
    except:
        return False
    if 0 < int(points) < 12:
        sql = "INSERT INTO points (user_id, song_id, points) VALUES (:user_id, :song_id, :points)"
        database.session.execute(sql, {"user_id":user_id, "song_id":country_id, "points":points})
        database.session.commit()
        return True
    else:
        return False


def get_all_points():
    user_id = users.user_id()
    if user_id == 0:
        return None
    sql = "SELECT C.name, P.points FROM countries C, points P WHERE user_id=:user_id AND C.id=P.song_id"
    result = database.session.execute(sql, {"user_id":user_id})
    return result.fetchall()