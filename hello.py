from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/repositories")
def hello():
    return render_template("repositories.html")


@app.route("/user/<string:username>")
def show_username(username):
    return f"User {username} should go swimming"
