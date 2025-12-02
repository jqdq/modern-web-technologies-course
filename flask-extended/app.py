from flask import Flask, render_template, abort, request, flash, g
import sys

# movie_ratings is just a mockup for a database.
# It's not connected to SQLAlchemy or anything, we just use it to populate the database in the beginning.
from movie_ratings import ratings

# We import the database connector from init_db.py
from models.init_db import db
from models.movie import Movie
from models.tag import Tag
from models.award import Award
from models.user import User
from auth import auth, login_required
from flask_wtf import CSRFProtect

app = Flask(__name__)
# Secret key is needed for flash messages and sessions to work.
# It's used to encrypt the data stored in the user's browser.
app.secret_key = b"fgfxnfykxjxtjr"
# Setting up the database location.
# Look for a file named 'db.db' in the 'instance' folder. That's the DB!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
# Initializing the database with the Flask app.
app.register_blueprint(auth)
db.init_app(app)

csrf = CSRFProtect(app)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/details/<int:movie_id>")
def details_page(movie_id):
    # You can easily retrieve a single object by its primary key using get_or_404.
    movie = db.get_or_404(Movie, movie_id)
    return render_template("details.html", movie=movie)


@app.get("/add")
@login_required
def add_movie():
    return render_template("add.html")


@app.post("/add")
@login_required
def add_movie_form():
    # Check if a movie with the given title already exists in the database.
    movie_name = request.form["title"]
    movies_with_title = db.session.execute(
        db.select(Movie).where(Movie.name == movie_name)
    ).scalar()
    if movies_with_title:
        # If it does, flash a message and re-render the add movie page.
        flash("Ten film jest już w bazie danych")
        return render_template("add.html")
    # Retrieving form data.
    cat_death = "cat_death" in request.form
    violence = "violence" in request.form
    loud_noises = "loud_noises" in request.form
    jump_scares = "jump_scares" in request.form

    user_id = g.user.id

    # Creating and adding the Movie object to the database.
    movie_object = Movie(
        name=movie_name,
        cat_death=cat_death,
        violence=violence,
        loud_noises=loud_noises,
        jump_scares=jump_scares,
        created_by_id=user_id,
    )
    db.session.add(movie_object)
    # Committing the changes to the database, so the movie gets an ID.
    db.session.commit()

    # Quick fix, since I noticed the award input wasn't working when
    awards_text = request.form["award"] + ", "
    tags_text = request.form["tag"] + ", "

    # Creating and adding Award objects to the database.
    award_names = awards_text.split(",")
    for award_name in award_names:
        clean_award_name = award_name.strip()
        # Skip empty award names
        if len(clean_award_name) == 0:
            continue

        # Creating the Award object and linking it to the movie.
        award_object = Award(award_name=clean_award_name, movie_id=movie_object.id)
        db.session.add(award_object)
    # Not comitting yet, as we don't need the ID of the Award objects.
    # We will commit later after adding tags.

    # Creating and adding the MovieTag objects to the database.
    for tag_name in tags_text.split(","):
        clean_tag_name = tag_name.strip()
        # Skip empty tags
        if len(clean_tag_name) == 0:
            continue

        # Check if the tag already exists
        existing_tag = db.session.execute(
            db.select(Tag).where(Tag.tag_name == clean_tag_name)
        ).scalar_one_or_none()  # Get existing tag or None

        # If the tag doesn't exist, create it
        if existing_tag is None:
            existing_tag = Tag(tag_name=clean_tag_name, movies=[movie_object])
            db.session.add(existing_tag)
        existing_tag.movies.append(movie_object)
        # Or you can do it this way:
        # movie_object.tags.append(existing_tag)
        # You can use other list methods like extend, remove, etc.
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

    # I added some code so we can filter by tags as well.
    include_tags = request.args.get("include_tags", "").lower().split(",")
    exclude_tags = request.args.get("exclude_tags", "").lower().split(",")

    # We can build the query step by step
    query_stmt = db.select(Movie).where(Movie.name.contains(query))

    # Now we add filtering by include_tags
    # Basically, we're appending to the query statement.
    # Movie must have ALL of these tags
    for tag_name in include_tags:
        if tag_name.strip():  # Skip empty strings
            query_stmt = query_stmt.where(
                # Check if the movie has a tag with the given name
                Movie.tags.any(Tag.tag_name == tag_name.strip())
            )

    # Now we add filtering by exclude_tags
    # Movie must NOT have ANY of these tags
    for tag_name in exclude_tags:
        if tag_name.strip():  # Skip empty strings
            query_stmt = query_stmt.where(
                # Check if the movie does NOT have a tag with the given name
                ~Movie.tags.any(Tag.tag_name == tag_name.strip())
            )

    results = db.session.execute(query_stmt).scalars()
    return render_template("search.html", results=results)


@app.get("/tag/<int:tag_id>")
def movie_tag(tag_id):
    result = db.get_or_404(Tag, tag_id)
    return render_template("tag.html", tag_name=result.tag_name, results=result.movies)


# Error handler for 404 Not Found errors.
# This will return a custom message when a page is not found.
@app.errorhandler(404)
def handle_not_found(req):
    return "?????????", 404


# Entry point of the application.
if __name__ == "__main__":
    command = sys.argv[1]
    # Setup command initializes the database and inserts data from movie_ratings.py
    # Use "python app.py setup" to run it.
    if command == "setup":
        with app.app_context():
            # This creates the database tables based on the models defined.
            db.create_all()
            # Creating a tag "all" to assign to all movies, just for demonstration.
            all_tag = Tag(tag_name="all")
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
                movie_object.tags.append(all_tag)
                db.session.add(movie_object)
            db.session.commit()
    # Serve command runs the Flask development server.
    # Use "python app.py serve" to run it.
    elif command == "serve":
        app.run(debug=True)
