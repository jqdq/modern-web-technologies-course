# Does the cat die?

Remember to install Flask using `pip install flask flask-wtf`

## Docs

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/templates/)

## Tasks for today

The blueprint is set up **not** to use a database, instead relying on lists. However, I strongly encourage you to try and migrate the project into SQLite. You'll find the appropriate solution on the solutions branch in the `flask-with-db` folder.

1. Start the development server using `flask run`.
2. Using [routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing) and the provided `movie_ratings.py` display details info for the movies.
3. Using [site rendering](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates), display the provided template.
   1. Use the `render_template` function.
   2. Modify the template so it uses the provided data
   3. Based on `index.html`, create a `base.html` site with:
      1. A `header` block,
      2. A `content` block (the content of the `<main>` tag),
      3. A `title` block (`<title>` in the `<head>`).
   4. Use the base in all the sites we're about to create.
4. Implement the search.
   1. Create a get request route, that retrieves the `query` parameter, as shown here:
   ```python
   query_string = request.args.get('query', '')
   ```
   2. On the site, List all the movies that contain the `query` string in them.
   3. Using the `url_for([function name], [parameters])` function (as described [here](https://www.geeksforgeeks.org/flask-url-helper-function-flask-url_for/)), add links to the movie details.
5. Using `add.html`, create a site for adding new movies:
   1. Create a GET and POST request route for retrieving the site and sending in data (explained [here](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods)).
   2. Retrieve the form data using `request.form[...]` (explained [here](https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object)).
   3. Save the data to the dictionary.
   4. Verify if the search works.
6. Add user management. The code is already prepared for you.
   1. Add the [blueprint](https://flask.palletsprojects.com/en/stable/tutorial/views/#create-a-blueprint) to the app.
   2. Add `CSRFProtect` from the `flask-wtf` package, using `csrf = CSRFProtect(app)`
   3. Add a secret key, using `app.secret_key = "..."`
   4. Admire my enormous skills:
      1. Look into the forms, notice how they use [CSRF tokens](https://www.geeksforgeeks.org/csrf-protection-in-flask/) (wow!).
      2. Look into the `auth.py`, notice how `load_logged_in_user()` is executed before every request (cool!).
      3. See how even without it, the session automatically manages the user id (slay!). This however requires using the **secret key**.
      4. Look into the password management, and notice how we do not save the password in our database (omg!).
   5. Make movie submission only possible to logged in users (see the `login_required` decorator in `auth.py`).
   6. Make it so only the appropriate links show up in the header. You can do it by checking for `g.user` in the template.
7. Look into the static content on the site:
   1. Notice how the CSS and the favicon was added automatically.
   2. Convert it, so it uses `url_for("static", ...)`
   3. Do the same with the other links on the site.

## Credits
Huge thanks to:
- My GF for giving me the idea for today's project
- [Pallets](https://github.com/pallets/flask/tree/3.1.0/examples/tutorial) for developing the tutorial project I stole the auth stuff from
- [GeeksForGeeks](https://www.geeksforgeeks.org/csrf-protection-in-flask/) for explaining `flask-wtf` very easily
- [pico.css](https://picocss.com/) for the beautiful classless CSS
- [favicon.io](https://favicon.io/emoji-favicons/cat/) for the favicon kitten
- [Does the Dog Die?](https://www.doesthedogdie.com/) for being the original animal death site.