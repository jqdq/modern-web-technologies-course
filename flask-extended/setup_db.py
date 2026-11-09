"""
Setup script: creates the SQLite database and fills it with initial data.

TODO: This is a skeleton for you to fill in. Follow the "Tasks - SQLite"
section in the README. Run it with `python setup_db.py` (NOT `flask setup` -
we are not using the Flask CLI in this project).
"""

from flask import Flask

from movie_ratings import ratings

app = Flask(__name__)


def setup_database():
    # TODO:
    # 1. Connect to the SQLite database file (the `sqlite3` module).
    #    Decide where the file should live, e.g. `instance/db.db`.
    # 2. Execute the schema file (CREATE TABLE ... statements) that you wrote,
    #    e.g. with `conn.executescript(open("schema.sql").read())`.
    # 3. Insert the movies from the `ratings` dictionary using INSERT
    #    statements with `?` placeholders.
    # 4. Commit and close the connection.
    raise NotImplementedError("Fill in setup_database() - see the README tasks")


if __name__ == "__main__":
    with app.app_context():
        setup_database()
        print("Database created and filled with initial data.")
