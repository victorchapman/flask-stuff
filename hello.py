from flask import Flask, render_template, request
from markupsafe import escape
import requests, os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/repositories", methods=["GET"])
def repositories():
    repos = request.json
    a_value = repos["https://disease.sh/v3/covid-19/countries/usa"]
    return render_template("repositories.html", a_value=a_value)


@app.route("/images")
def images():
    return render_template("images.html")


@app.route("/user/<string:username>")
def show_username(username):
    return f"User {username} should go swimming"
