"""Copyright 2010 Pallets"""
import functools
import sqlite3

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        user = cursor.execute("SELECT id, username, password FROM Users WHERE id = ?", (user_id,)).fetchone()
        db.close()
        g.user = {
            "id": user[0],
            "username": user[1],
            "password": user[2]
        }


@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        if error is None:
            cursor.execute("SELECT id FROM Users WHERE username = ?", (username,))
            if cursor.fetchone() is not None:
                error = "User is already registered."
            else:
                cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))

                db.commit()
                db.close()
                # Success, go to the login page.
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        user = cursor.execute("SELECT id, password FROM Users WHERE username = ?", (username,)).fetchone()
        db.close()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user[1], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user[0]
            return redirect(url_for("home"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("home"))