"""
Authentication blueprint for user login, registration, and session management.
Includes a decorator to protect routes that require authentication.

You can use this file with minimal changes in your own projects to add user authentication.
"""

import functools
from flask import Blueprint, request, flash, redirect, url_for, session, g
from flask import render_template

# Workzeug is the underlying server library used by Flask.
from werkzeug.security import check_password_hash, generate_password_hash

from models.user import User
from models.init_db import db

# Blueprints help us organize the app into smaller components.
auth = Blueprint("auth", __name__, url_prefix="/auth")


# Decorators are functions that wrap other functions to modify their behavior.
# This decorator checks if a user is logged in before allowing access to the route.
def login_required(route):

    @functools.wraps(route)
    def wrapped_view(**kwargs):
        # You can easily check for more stuff here, like wether the user has
        # the right permissions to access the route.
        # You can also perform these checks in the controller itself.
        if g.user is None:
            return redirect(url_for("auth.login_page"))

        return route(**kwargs)

    return wrapped_view


# Before each request, we load the logged-in user from the session.
@auth.before_app_request
def load_logged_in_user():
    # Retrieve user_id from the session cookie
    user_id = session.get("user_id")
    # g is an object storing data between methods during a request.
    # We use it to store the logged-in user, so other methods do not have to query the DB again.
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
    # Retrieve form data
    username = request.form["username"]
    password = request.form["password"]

    # Flash message if username or password is empty
    if username == "":
        flash("Please enter a username")
        return login_page()
    if password == "":
        flash("Please enter a password")
        return login_page()

    # Query the user from the database
    user = db.session.execute(
        db.select(User).where(User.username == username)
    ).scalar_one_or_none()

    # Check if user exists
    if not user:
        flash("Incorrect login or password")
        return login_page()

    # Since we store hashed passwords, we cannot compare them directly.
    # We use check_password_hash to verify the password.
    if not check_password_hash(user.password, password):
        flash("Incorrect login or password")
        return login_page()

    # Set up the user session and redirect to home page
    session.clear()
    session["user_id"] = user.id
    return redirect(url_for("home"))


@auth.get("/register")
def register_page():
    return render_template("auth/register.html")


@auth.post("/register")
def register_process():
    # Retrieve form data
    username = request.form["username"]
    password = request.form["password"]

    # Flash message if username or password is empty
    if username == "":
        flash("Please enter a username")
        return register_page()
    if password == "":
        flash("Please enter a password")
        return register_page()

    # Check if the username is already taken
    username_used = db.session.execute(
        db.select(User).where(User.username == username)
    ).scalar()
    if username_used:
        flash("Username is already taken")
        return register_page()

    # Create a new user with hashed password and add to the database
    # We have to hash the password before storing it to defend against password leaks.
    # This way, even if the database is compromised (or someone just looks at it),
    # the actual passwords are not shown.
    # Notice inputing the password hash into the form will not work, as the hash
    # function is one-way. You have to input the original password to log in.
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    # Set up the user session and redirect to home page
    session.clear()
    session["user_id"] = user.id
    return redirect(url_for("home"))


@auth.route("/logout")
def logout():
    # Clear the user session to log out
    session.clear()
    return redirect(url_for("home"))
