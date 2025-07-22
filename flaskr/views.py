from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from .models import User, Time
from . import db

views = Blueprint("views", __name__)


@views.route
@views.route("/home")
def home():
    return render_template("home.html", user=current_user)


@views.route("/timer")
def timer():
    return render_template("timer.html", user=current_user)


@views.route("/times", methods=["POST", "GET"])
def times():
    if request.method == "POST":
        data = request.get_json()
        newTime = Time(
            timestamp=data["date"], value=data["value"], user_id=current_user.id)
        db.session.add(newTime)
        db.session.commit()
        print("added new time")
        return "", 204
    else:
        times_list = []
        if current_user.is_authenticated:
            for time in current_user.times:
                times_list.append(
                    {"date": time.timestamp, "value": time.value})
            return jsonify(times_list), 200
        else:
            return jsonify({"error": "User not found"}), 404


@views.route("/check-auth")
def check_auth():
    if current_user.is_authenticated:
        return jsonify({"authenticated": True}), 200
    return jsonify({"authenticated": False}), 200
