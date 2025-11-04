# Does the cat die? with an actual DB

Remember to install Flask using `pip install Flask-SQLAlchemy`

## Docs

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/templates/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [Flask SQLAlchemy plugin](https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/)
- [GeeksForGeeks tutorial](https://www.geeksforgeeks.org/python/sqlalchemy-tutorial-in-python/)

## Tasks for today

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
9. Add a `Director` model and create a one-to-many relationship. Use it to implement the director page and director list. Order them by movie counts (use `join`/`outer_join`, `group_by`, and `func`).
10. Insert data from `movie_ratings.py` on initialization.
11. Add tags to movies, implement them using a many-to-many relationship. More [here](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many)! Remember to use `db.Table` instead.

Also check this out:
https://flask-sqlalchemy.readthedocs.io/en/stable/pagination/

## Credits
Huge thanks to:
- My GF for giving me the idea for today's project
- [pico.css](https://picocss.com/) for the beautiful classless CSS
- [favicon.io](https://favicon.io/emoji-favicons/cat/) for the favicon kitten
- [Does the Dog Die?](https://www.doesthedogdie.com/) for being the original animal death site.