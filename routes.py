from app import app
from flask import render_template, request, redirect, flash, abort, session
from secrets import token_hex
import users
import countries
import user_content


@app.route("/")
def index():
        return render_template("front_page.html")


@app.route("/login", methods=["GET","POST"])
def login():
        error = None
        if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]

                if users.login(username, password):
                        return redirect("/")
                else:
                        error = "Väärä käyttäjänimi tai salasana"
        
        return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
        error = None

        if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]

                if len(username) > 40:
                        error = "Käyttäjänimen tulee olla alle 40 merkkiä"
                elif len(username) < 1:
                        error = "Käyttäjänimen tulee olla vähintään yhden merkin mittainen"
                if len(password) > 40:
                        error = "Salasana saa olla enintään 40 merkkiä"
                elif len(password) < 8:
                        error = "Salasanan tulee olla vähintään kahdeksan merkkiä"
                if not users.is_username_available(username):
                        error = "Käyttäjänimi varattu"

                if error is None:
                        if users.register(username,password):
                                flash("Rekisteröityminen onnistui")
                                return redirect("/")
                        else:
                                error = "Rekisteröityminen epäonnistui."

        return render_template("register.html", error=error)


@app.route("/logout")
def logout():
        users.logout()
        return redirect("/")


@app.route("/list", methods=["GET","POST"])
def list_page():
        if request.method == "GET":
                return render_template("country_list.html", countries=countries.get_list())
        
        if request.method == "POST": 

                country = request.form["country"]
                id = countries.country_id(country)
                return redirect(f"/country/{id}")


@app.route("/country/<int:id>", methods=["GET", "POST"])
def country_page(id):
        error = None
        country = countries.country_name(id)
        song = countries.song_and_singer(id)
        points = user_content.get_points(id)
        messages = user_content.get_messages(id, None)

        if request.method == "POST":
                message = request.form["message"]
                if session["csrf_token"] != request.form["csrf_token"]:
                        abort(403)
                if not user_content.send_message(message, id):
                        error = "Virhe kommentin lähettämisessä. Tarkista ettei viestisi ole tyhjä tai liian pitkä."
                else:
                        return redirect(f"/country/{id}")

        return render_template("song.html", id=id, song=song, country=country, points=points, messages=messages, error=error)


@app.route("/points/<int:id>", methods=["GET","POST"])
def points(id):
        error = None
        update_ability = user_content.can_update_points(id)

        if request.method == "POST":
                points = request.form["points"]
                if session["csrf_token"] != request.form["csrf_token"]:
                        abort(403)

                if not update_ability:
                        if not user_content.add_points(points, id):
                                error = "Virhe pisteiden lisäämisessä. Huom. pisteet tulee olla väliltä 0-12 ja kirjoitettuna numeroina."
                        else:
                                return redirect(f"/country/{id}")

                else:
                        if not user_content.update_points(points, id):
                                error = "Virhe pisteiden päivittämisessä. Huom. pisteet tulee olla väliltä 0-12 ja kirjoitettuna numeroina."
                        else:
                                return redirect(f"/country/{id}")

        return render_template("points.html", id=id, error=error)


@app.route("/delete/<int:id>")
def delete_message(id):
        error = None
        user_id = users.user_id()

        if user_id == 0 or users.is_admin(user_id) is False:
                error = "Ei oikeutta nähdä tätä sivua"
        else:
                if user_content.delete_comment(id):
                        return redirect("/list")

        return render_template("delete_message.html", error=error)
        


@app.route("/user/<int:user_id>", methods=["GET"])
def user_page(user_id):
        error = "Ei oikeutta nähdä tätä sivua"

        if users.user_id() != 0:
                error = None

        return render_template("user_page.html", countries=user_content.get_all_points(), messages=user_content.get_messages(None, user_id), error=error)
