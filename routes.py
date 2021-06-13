from app import app
from flask import render_template, request, redirect, flash
import users
import countries

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

@app.route("/list")
def list_page():
        #if request.method == "GET":
        return render_template("country_list.html", countries=countries.get_list())
        
        #if request.method == "POST": 
                #country = request.form[""]

@app.route("/country/<int:id>")
def country_page(id):
        return render_template("song.html", id=id)
