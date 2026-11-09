"""
Authentication blueprint for user login, registration, and session management.
It also includes a decorator that protects routes requiring a logged-in user.

TODO: This is a skeleton for you to fill in. Follow the "Authentication" tasks
in the README. You can use this file with minimal changes in your own projects.
"""

import functools
import secrets
from flask import (
    Blueprint,
    request,
    flash,
    redirect,
    url_for,
    session,
    g,
    render_template,
)

# Werkzeug is the underlying server library used by Flask.
# TODO: once you reach the password storage task, import:
# from werkzeug.security import check_password_hash, generate_password_hash

# Blueprints help us organize the app into smaller components.
# This one groups all /auth/... routes (e.g. /auth/login, /auth/register).
auth = Blueprint("auth", __name__, url_prefix="/auth")


# Decorators are functions that wrap other functions to modify their behavior.
# This decorator checks if a user is logged in before allowing access to a route.
# TODO: fill in the session check (see README, Authentication task 6).
def login_required(route):

    @functools.wraps(route)
    def wrapped_view(**kwargs):
        # TODO: check if a user id is stored in the session.
        # If not, redirect the user to the login page.
        # Hint: session.get("user_id")
        return route(**kwargs)

    return wrapped_view


# Runs before every request, so the logged-in user (if any) is available
# to all templates and views as `g.user`.
# TODO: fill in the user lookup (see README, Authentication task 7).
@auth.before_app_request
def load_logged_in_user():
    # g is an object storing data for the duration of a single request.
    g.user = None
    # TODO: retrieve user_id from the session and load the matching user
    # from the database into g.user.


# Not every visitor registers - we still want to remember things like the
# search history, theme preference or "movies viewed" count for them.
# For that we store an anonymous visitor id in a cookie, and expose it
# through `g` (README, Authentication task 8).
#
# Why `g`? Views and templates then just use `g.visitor_id` and never
# touch cookies directly. It also mirrors how `g.user` works above:
# "before the request" loads data into g, and the cookie is written
# "after the request", when we have a response to attach it to.
@auth.before_app_request
def load_visitor_id():
    # Read the visitor id from the cookie (None if the browser didn't send one).
    g.visitor_id = request.cookies.get("visitor_id")
    if g.visitor_id is None:
        # Generate one now, so this request can already use it.
        # secrets.token_hex is a cryptographically secure random string.
        g.visitor_id = secrets.token_hex(16)


@auth.after_app_request
def remember_visitor(response):
    # Only set the cookie if the browser didn't send one - after this
    # response, it will send it back with every following request.
    # httponly: JavaScript cannot read it (defense against XSS).
    # samesite: it is not sent with cross-site requests (defense against CSRF).
    if "visitor_id" not in request.cookies:
        response.set_cookie(
            "visitor_id", g.visitor_id,
            max_age=60 * 60 * 24 * 30,  # 30 days
            httponly=True, samesite="Lax",
        )
    return response


@auth.get("/login")
def login_page():
    return render_template("auth/login.html")


@auth.post("/login")
def login_process():
    # TODO: see README, Authentication task 4.
    flash("Login is not implemented yet")
    return login_page()


@auth.get("/register")
def register_page():
    return render_template("auth/register.html")


@auth.post("/register")
def register_process():
    # TODO: see README, Authentication task 3.
    flash("Register is not implemented yet")
    return register_page()


@auth.route("/logout")
def logout():
    # TODO: remove the user id from the session (see README, task 5).
    return redirect(url_for("home"))
