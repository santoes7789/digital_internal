from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")


@views.route("/timer")
def timer():
    return render_template("timer.html")
