from app import app
from flask import render_template, request, redirect
import users


@app.route("/")
def index():
        return render_template("front_page.html")


@app.route("/login", methods=["GET","POST"])
def login():

        if request.method == "GET":
                return render_template("login.html")

        if request.method == "POST":
                kayttajanimi = request.form["username"]
                salasana = request.form["password"]

                if users.login(kayttajanimi, password):
                        return redirect("/")
                else:
                        return redirect("/")


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
                        return redirect("/")

