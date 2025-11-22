from flask import Flask, render_template, abort, request, flash
import sys

# movie_ratings is just a mockup for a database.
# It's not connected to SQLAlchemy or anything, we just use it to populate the database in the beginning.
from movie_ratings import ratings, directors

# We import the database connector from init_db.py
from models.init_db import db
from models.movie import Movie
from models.tag import MovieTag

app = Flask(__name__)
# Secret key is needed for flash messages and sessions to work.
# It's used to encrypt the data stored in the user's browser.
app.secret_key = b"fgfxnfykxjxtjr"
# Setting up the database location.
# Look for a file named 'db.db' in the 'instance' folder. That's the DB!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
# Initializing the database with the Flask app.
db.init_app(app)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/details/<int:movie_id>")
def details_page(movie_id):
    # You can easily retrieve a single object by its primary key using get_or_404.
    movie = db.get_or_404(Movie, movie_id)
    return render_template("details.html", movie=movie)


@app.get("/add")
def add_movie():
    # Directors dictionary is imported from movie_ratings.py. We'll have to change it.
    return render_template("add.html", directors=directors)


@app.post("/add")
def add_movie_form():
    # Check if a movie with the given title already exists in the database.
    movie_name = request.form["title"]
    movies_with_title = db.session.execute(
        db.select(Movie).where(Movie.name == movie_name)
    ).scalar()
    if movies_with_title:
        # If it does, flash a message and re-render the add movie page.
        flash("Ten film jest już w bazie danych")
        return render_template("add.html", directors=directors)
    # Retrieving form data.
    cat_death = "cat_death" in request.form
    violence = "violence" in request.form
    loud_noises = "loud_noises" in request.form
    jump_scares = "jump_scares" in request.form
    tag = request.form["tag"]

    # Creating and adding the Movie object to the database.
    movie_object = Movie(
        name=movie_name,
        cat_death=cat_death,
        violence=violence,
        loud_noises=loud_noises,
        jump_scares=jump_scares,
    )
    db.session.add(movie_object)
    # Committing the changes to the database, so the movie gets an ID.
    db.session.commit()

    # Creating and adding the MovieTag objects to the database.
    for i in tag.split(","):
        # Skip empty tags
        if len(i) == 0:
            continue
        movie_tag_object = MovieTag(tag_name=i, movie_id=movie_object.id)
        db.session.add(movie_tag_object)
    db.session.commit()

    # Redirecting to the details page of the newly added movie.
    return details_page(movie_object.id)


@app.get("/search")
def search_movies():
    # Retrieving the search query from the URL parameters.
    # Query is the ?query=... part of the URL.
    # These are used when defining a GET form in HTML:
    # https://www.w3schools.com/tags/att_form_method.asp
    query = request.args.get("query", "").lower()
    # Searching for movies that contain the query string in their name.
    results = db.session.execute(  # Execute a database query
        db.select(  # The query is a SELECT statement
            Movie  # Select will be on the Movie table
        ).where(
            Movie.name.contains(query)
        )  # We want to filter by the name attribute containing the query
    ).scalars()  # .scalars() extracts the Movie objects from the result
    return render_template("search.html", results=results)


@app.get("/tag")
def movie_tag():
    query = request.args.get("query", "").lower()
    results = db.session.execute(  # Execute a database query
        db.select(Movie)  # Select will be on the Movie table
        .join(MovieTag)  # Join with MovieTag table, as specified in the model
        .where(
            MovieTag.tag_name == query
        )  # We want to filter by the tag_name attribute matching the query
    ).scalars()  # .scalars() extracts the Movie objects from the result
    return render_template("search.html", results=results)


# Entry point of the application.
if __name__ == "__main__":
    command = sys.argv[1]
    # Setup command initializes the database and inserts data from movie_ratings.py
    # Use "python app.py setup" to run it.
    if command == "setup":
        with app.app_context():
            # This creates the database tables based on the models defined.
            db.create_all()
            # Inserting data from movie_ratings.py
            # The Object(...), db.session.add(...), and db.session.commit()
            # pattern is how you add data to the database.
            for movie in ratings.values():
                movie_object = Movie(
                    name=movie["title"],
                    cat_death=movie["cat_death"],
                    violence=movie["violence"],
                    loud_noises=movie["loud_noises"],
                    jump_scares=movie["jump_scares"],
                )
                db.session.add(movie_object)
            db.session.commit()
    # Serve command runs the Flask development server.
    # Use "python app.py serve" to run it.
    elif command == "serve":
        app.run(debug=True)
