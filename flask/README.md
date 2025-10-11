# Does the cat die?

## Running the project

1. Download the repository (using git or unpack the zip)
2. Open the flask folder in VS Code:
   1. Open the File menu
   2. Click on "Open folder..."
   3. Find the course directory (usually named `modern-web-technologies-main`)
   4. Select the `flask` folder inside it
3. Install flask using `pip install flask`.
4. Ensure you have the flask folder opened in your terminal (the path should contain `modern-web-technologies-main/flask`).
5. Run the development server using `flask run`/`python app.py`

## Docs

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Jinja](https://jinja.palletsprojects.com/en/stable/templates/)

## Tasks for today

The blueprint is set up **not** to use a database, instead relying on lists. However, I strongly encourage you to try and migrate the project into SQLite. You'll find the appropriate solution on the solutions branch in the `flask-with-db` folder.

1. Using `render_template` render the `index.html` file.
2. Using [routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing) and the provided `movie_ratings.py` display details info for the movies.
3. Listen to Kuba explain route groups, it's useful!
4. Using [site rendering](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates), display the provided template.
   1. Use the `render_template` function.
   2. Modify the template so it uses the provided data
   3. Based on `index.html`, create a `base.html` site with:
      1. A `header` block,
      2. A `content` block (the content of the `<main>` tag),
      3. A `title` block (`<title>` in the `<head>`).
   4. Use the base in all the sites we're about to create.
   5. Convert all the links to `url_for([function name], [parameters])` (as described [here](https://www.geeksforgeeks.org/flask-url-helper-function-flask-url_for/))
5. Implement the search.
   1. Create a get request route, that retrieves the `query` parameter, as shown here:
   ```python
   query_string = request.args.get('query', '')
   ```
   2. On the site, List all the movies that contain the `query` string in them.
6. Using `add.html`, create a site for adding new movies:
   1. Create a GET and POST request route for retrieving the site and sending in data (explained [here](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods)).
   2. Retrieve the form data using `request.form[...]` (explained [here](https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object)).
   3. Save the data to the dictionary.
   4. Verify if the search works.
7. Set up the static content for the site.
   1. Set up the static files directory.
   2. Migrate links to url_for.
   3. Add images for the movies.
8.  Scare user by telling him what device is he using.

## Credits
Huge thanks to:
- My GF for giving me the idea for today's project
- [pico.css](https://picocss.com/) for the beautiful classless CSS
- [favicon.io](https://favicon.io/emoji-favicons/cat/) for the favicon kitten
- [Does the Dog Die?](https://www.doesthedogdie.com/) for being the original animal death site.