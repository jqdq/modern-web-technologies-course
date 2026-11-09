# Does the cat die? with an actual DB

Remember to install Flask using `pip install flask`.

## Running the project

1. Open the `flask-extended` folder in VS Code / your terminal.
2. Install flask using `pip install flask`.
   No need to install SQLite: Python's built-in `sqlite3` module already
   bundles the whole database engine - `import sqlite3` just works.
3. Run the development server: `python app.py`

> We are **not** using the Flask CLI (`flask ...` commands) in this project.
> Everything the CLI would do is done by plain Python scripts instead.

## Docs

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/templates/)
- [sqlite3 - built-in Python interface for SQLite](https://docs.python.org/3/library/sqlite3.html)
- [SQLite itself](https://sqlite.org/lang.html) (SQL syntax reference)
- [Flask tutorial: the same app built on raw sqlite3](https://flask.palletsprojects.com/en/stable/tutorial/)

## Tasks for today - SQLite

1. Create a `schema.sql` file with `CREATE TABLE` statements for:
   - `movie` (id, name, cat_death, violence, loud_noises, jump_scares, created_by)
   - `user` (id, username, password)
   - `tag` (id, tag_name)
   - `award` (id, award_name, movie_id) - movie_id is a foreign key to `movie`, used in the Many-to-One task below
   - `movie_tag` (movie_id, tag_id) - the association table for the Many-to-Many relationship, described below
2. Connect to the database using:
   ```python
   import sqlite3
   connection = sqlite3.connect("instance/db.db")
   connection.row_factory = sqlite3.Row  # lets you access columns by name
   ```
   Since every request needs its own connection, wrap this in a `get_db()`
   helper and register `teardown_appcontext` to close it (like in the
   [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/database/)).
3. Fill in `setup_db.py`:
   1. Execute the schema from `schema.sql` (`connection.executescript(...)`).
   2. Insert the data from `movie_ratings.py` using `INSERT` statements.
   3. Commit and close the connection.
   4. Run it with `python setup_db.py`. Delete the `db.db` file and re-run it whenever you change the schema.
   5. See the records you just inserted: install the [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
      VS Code extension and click on `db.db`. Do this after every task - watching the
      tables change as the app runs is the best way to understand what your SQL does.
4. Rebuild the Add movie functionality using `INSERT` with `?` placeholders:
   ```python
   connection.execute(
       "INSERT INTO movie (name, cat_death, ...) VALUES (?, ?, ...)",
       (name, cat_death, ...),
   )
   connection.commit()
   ```
   Placeholders are non-negotiable - they are your defense against
   SQL injection (discussed below).
5. Implement the movie page using `SELECT ... WHERE id = ?`.
   `fetchone()` returns a single row (or `None` - flash a 404 then).
6. Implement the search using `SELECT ... WHERE name LIKE ?` and `ORDER BY`.
7. Add tags to movies as a **Many-to-Many** mapping:
   - A movie can have many tags, and a tag can be on many movies.
   - Neither table can store a foreign key to the other (which side would it be?),
     so we use the `movie_tag` association table - two foreign keys, one row per connection:
     ```sql
     SELECT tag.* FROM tag
     JOIN movie_tag ON tag.id = movie_tag.tag_id
     WHERE movie_tag.movie_id = ?;
     ```
   - Add a comma-separated "Tags" input to the Add movie form, so a new movie
     gets its tags right away.
   - Use Many-to-Many for things like: tags/filters on objects,
     user roles and permissions, students and classes, products and orders.
8. Add awards to movies as a **Many-to-One** mapping:
   - One movie can win many awards, but each award belongs to exactly one movie.
   - Unlike Many-to-Many, this needs no association table - a single foreign key
     on the "many" side (the `movie_id` column of the `award` table) is enough:
     ```sql
     SELECT award.award_name FROM award
     JOIN movie ON award.movie_id = movie.id
     WHERE movie.id = ?;
     ```
   - Add a comma-separated "Awards" input to the Add movie form, split it in the
     view and insert one `award` row per name - just like in the `flask` folder's
     word list exercises, but into the database.
   - Display the awards on the movie page, next to the tags.
   - Use Many-to-One for things like: categories (one per object),
     ownership (a user owns many posts, each post has one owner),
     comments on a post, orders with one status.

Also check this out:
- [Pagination in raw SQL](https://sqlite.org/lang_select.html#limitoffset): `LIMIT ? OFFSET ?`

## Tasks for today - Authentication

1. Create the `user` table (if you haven't in the SQL tasks).
2. Write the register logic (in `auth.py`):
   1. Retrieve username and password from the form.
   2. Flash an error if they are missing.
   3. Check if username is taken (`SELECT ... WHERE username = ?`) and flash if true.
   4. Store the username and password hash (`generate_password_hash` from `werkzeug.security`) in the database.
   5. Set the session user ID.
   6. Redirect the user to the main page.
3. Write the login logic:
   1. Retrieve username and password from the form.
   2. Flash an error if they are missing.
   3. Retrieve the user from the database. Flash if no user exists.
   4. Check the password (`check_password_hash`).
   4. Set the session user ID.
4. Write the logout logic:
   1. Remove the user id from session.
   2. Redirect to homepage.
5. Write a `login_required` decorator (skeleton in `auth.py`), checking if the session user ID is set. If not, redirect to the login page.
   1. Only allow usage of the add movie form if user is logged in.
   2. Add an `author` column to the `movie` table. Show the username on the movie page.
6. Load user data into the `g` object by retrieving the user with a corresponding user ID (skeleton in `auth.py`).
   1. Add a user panel to the navbar (show the links only when a user is logged in/out).
   2. Optionally: create a user page with all movie pages authored by them.
7. Add CSRF protection:
   1. Install `flask-wtf`.
   2. In `app.py`, import `CSRFProtect`.
   3. Initialize it with the app object: `csrf = CSRFProtect(app)`.
   4. Uncomment the `<input type="hidden" name="csrf_token" ...>` in the auth forms and add it to the other forms.
8. Store an **anonymous user id and other functional data in `g`** (already set up in `auth.py` - read the comments there):
   1. Not every visitor registers - still, you may want to remember things like the
      search history, theme preference or a "movies viewed" counter without a login.
   2. The pattern is the same as for `g.user`: a `before_app_request` hook reads the
      `visitor_id` cookie into `g.visitor_id` (generating one via `secrets.token_hex(16)`
      if missing), and an `after_app_request` hook attaches the cookie to the response
      with:
      ```python
      response.set_cookie(
          "visitor_id", g.visitor_id,
          max_age=60 * 60 * 24 * 30,  # 30 days
          httponly=True, samesite="Lax",
      )
      ```
   3. Views and templates can now just use `g.visitor_id` - try it by showing
      "you are visitor #..." or storing the last searched query in another cookie.
   4. Discuss what belongs in a cookie: it's sent with every request, readable by the user,
      and (unlike the Flask `session`) **not signed** - never trust its contents, treat it like any other user input.
   5. Check what Flask's `session` cookie actually contains: `python -c "from itsdangerous import URLSafeSerializer; ..."`
      - it's just signed (tamper-proof), not encrypted. Don't store secrets in it.
9. Defend against **XSS when dealing with user-supplied HTML**:
   1. Add a rich "description" field where the user may write HTML (e.g. `<b>Shrek</b>`).
   2. Render it with `{{ movie.description|safe }}` and show how a `<script>alert(...)</script>`
      or `<img onerror=...>` steals the session cookie: `document.cookie`.
   3. Fix it with an allow-list sanitizer, e.g. [bleach](https://bleach.readthedocs.io/en/latest/):
      `bleach.clean(user_html, tags=["b", "i", "em", "strong", "p", "a"], attributes={"a": ["href"]})`.
   4. Note that Jinja autoescapes everything by default - `|safe` is the dangerous opt-out.
   5. Optionally: add a `Content-Security-Policy` header as a second line of defense.
10. Add **photo storage**:
    1. Add a poster upload to the Add movie form (`<input type="file" name="poster">` + `enctype="multipart/form-data"`).
    2. Save the file with `werkzeug.utils.secure_filename(file.filename)` into `static/uploads/`
       - **never** trust the raw filename (`../../app.py` is a valid filename).
    3. Store the path (not the bytes) in the `movie` table and display it with `url_for('static', filename=...)`.
    4. Limit size and extensions (`file.content_type`, `app.config["MAX_CONTENT_LENGTH"]`).
    5. Discuss alternatives: storing blobs in SQLite (`BLOB` columns) vs. files on disk vs. object storage (S3), and
       that for big apps the DB row should hold metadata while the bytes live elsewhere.
11. Add user groups as another **Many-to-Many** mapping (implemented with a `user_group` association table this time):
    1. Create `group` and `user_group` tables.
    2. Let users join groups and show the group members on a group page.
    3. Add a permission: only group members may edit movies added by other group members.

Remember to discuss:
- SQL Injection (and why `?` placeholders matter)
- XSS attacks (and autoescaping, sanitization, CSP)
- CSRFs (and why the token has to be a hidden field in *every* form)
- Password storage (hashing, salting - and why not plaintext or md5)
- Shoulder surfing attacks
- Cookies vs. sessions (what lives where, who can read/modify it)

## Credits
Huge thanks to:
- My GF for giving me the idea for today's project
- [pico.css](https://picocss.com/) for the beautiful classless CSS
- [favicon.io](https://favicon.io/emoji-favicons/cat/) for the favicon kitten
- [Does the Dog Die?](https://www.doesthedogdie.com/) for being the original animal death site.
