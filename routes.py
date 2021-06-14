from app import app
from flask import render_template, request, redirect, flash
import users
import countries
import user_content

@app.route("/")
def index():
        return render_template("front_page.html")


@app.route("/login", methods=["GET","POST"])
def login():

        if request.method == "GET":
                return render_template("login.html")

        if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]

                if users.login(username, password):
                        return redirect("/")
                else:
                        error = "Väärä käyttäjänimi tai salasana"
                        return render_template("error.html", message=error)


@app.route("/register", methods=["GET", "POST"])
def register():

        if request.method == "GET":
                return render_template("register.html")

        if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]

                if users.register(username,password):
                        return redirect("/")
                else:
                        message = "Rekisteröityminen epäonnistui."
                        return render_template("error.html", message=message)

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
        country = countries.country_name(id)
        song = countries.song_and_singer(id)
        points = user_content.get_points(id)
        messages = user_content.get_messages(id)
        
        if request.method == "POST":
                message = request.form["message"]
                if not user_content.send_message(message, id):
                        return render_template("error.html", message="Viestin lähettämisessä tapahtui virhe.")

        return render_template("song.html", id=id, song=song, country=country, points=points, messages=messages)


@app.route("/points/<int:id>", methods=["GET","POST"])
def points(id):
        if request.method == "POST":
                points = request.form["points"]
                if not user_content.add_points(points, id):
                        return render_template("error.html", message="Virhe pisteiden lisäämisessä")

        return render_template("points.html", id=id)

@app.route("/user/<int:user_id>", methods=["GET"])
def user_page(user_id):
        return render_template("user_page.html", countries=user_content.get_all_points())