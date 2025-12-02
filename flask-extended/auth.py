import functools
from flask import Blueprint, request, flash, redirect, url_for, session, g
from flask import render_template

from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from models.init_db import db

auth = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(route):

    @functools.wraps(route)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login_page"))

        return route(**kwargs)

    return wrapped_view


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        user = db.get_or_404(User, user_id)
        g.user = user


@auth.get("/login")
def login_page():
    return render_template("auth/login.html")


@auth.post("/login")
def login_process():
    username = request.form["username"]
    password = request.form["password"]
    if username == "":
        flash("Please enter a username")
        return login_page()
    if password == "":
        flash("Please enter a password")
        return login_page()

    user = db.session.execute(
        db.select(User).where(User.username == username)
    ).scalar_one_or_none()
    if not user:
        flash("Incorrect login or password")
        return login_page()

    if not check_password_hash(user.password, password):
        flash("Incorrect login or password")
        return login_page()

    session.clear()
    session["user_id"] = user.id
    return redirect(url_for("home"))


@auth.get("/register")
def register_page():
    return render_template("auth/register.html")


@auth.post("/register")
def register_process():
    username = request.form["username"]
    password = request.form["password"]
    if username == "":
        flash("Please enter a username")
        return register_page()
    if password == "":
        flash("Please enter a password")
        return register_page()

    username_used = db.session.execute(
        db.select(User).where(User.username == username)
    ).scalar()
    if username_used:
        flash("Username is already taken")
        return register_page()

    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    session.clear()
    session["user_id"] = user.id
    return redirect(url_for("home"))


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))
