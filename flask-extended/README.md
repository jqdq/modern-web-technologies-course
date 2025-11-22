# Does the cat die? with an actual DB

Remember to install Flask using `pip install Flask-SQLAlchemy`

## Docs

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/templates/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [Flask SQLAlchemy plugin](https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/)
- [GeeksForGeeks tutorial](https://www.geeksforgeeks.org/python/sqlalchemy-tutorial-in-python/)

## Tasks for today - SQL

1. Install `Flask-SQLAlchemy`
2. Connect to a database using:
    ```python
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
    db.init_app(app)
    ```
3. Create a model for the movies using the following notation:
    ```python
    from sqlalchemy.orm import Mapped, mapped_column

    class User(Base):
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(50), default="Test")
        fullname: Mapped[str | None]
        nickname: Mapped[str | None] = mapped_column(String(30))
    ```
4. Write a CLI command that will generate the appropriate table:
    ```python
    @app.cli.command("function-name")
    def function()
    ```
5. Use it to generate the table: `flask migrate`
6. Using [these](https://flask-sqlalchemy.readthedocs.io/en/stable/queries/#insert-update-delete) rebuild the Add movie functionality.
7. Implement the movie page using `db.get_or_404(...)`. More [here](https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/#query-the-data)!
8. Implement the search using `db.session.execute(db.select(...))`. Order them alphabetically. More [here](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html)!
9.  Insert data from `movie_ratings.py` on initialization.
10. Add tags to movies using Many-to-One joins.

Also check this out:
https://flask-sqlalchemy.readthedocs.io/en/stable/pagination/

## Tasks for today - Authentication

1. Create a user model
2. Create an auth [blueprint](https://flask.palletsprojects.com/en/stable/blueprints/).
3. Write the register logic:
   1. Retrieve username and password from the form
   2. Flash an error if they are missing.
   3. Check is username is taken and flash if true.
   4. Store the username and password hash (`generate_password_hash` from `werkzeug.security`) in the database.
   5. Set the session user ID.
   6. Redirect the user to the main page.
4. Write the login logic:
   1. Retrieve username and password from the form.
   2. Flash an error if they are missing.
   3. Retrieve the user from the database. Flash if no user exists.
   4. Check the password (`check_password_hash`).
   5. Set the session user ID.
5. Write the logout logic:
   1. Remove the user id from session.
   2. Redirect to homepage.
6. Write a `login_required` decorator, checking is the session user ID is set. If not, redirect to the login page.
   1. Only allow usage of the add movie form if user is logged in.
   2. Add an `author` field to the movie model. Show the username on the movie page.
7. Load user data into the `g` object by retrieving the user with a corresponding user ID.
   1. Add a user panel to the navbar.
   2. Add a logout, login and register buttons.
   3. Optionally: create a user page with all movie pages authored by them.
8. Add CSRF protection:
   1. Install `flask-wtf`.
   2. In `app.py`, import `CSRFProtect`
   3. Initialize it with the app object: `csrf = CSRFProtect(app)`.
   4. Add `<input type="hidden" name="csrf_token" value = "{{ csrf_token() }}"/> ` into the website forms.
9. Add user groups as Many-to-many relationships. Implement them using a one-to-many relationship. More [here](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many)!

Remember to discuss:
- SQL Injection
- XSS attacks (arbitrary code execution)
- CSRFs
- Password storage
- Shoulder surfing attacks

## Credits
Huge thanks to:
- My GF for giving me the idea for today's project
- [pico.css](https://picocss.com/) for the beautiful classless CSS
- [favicon.io](https://favicon.io/emoji-favicons/cat/) for the favicon kitten
- [Does the Dog Die?](https://www.doesthedogdie.com/) for being the original animal death site.