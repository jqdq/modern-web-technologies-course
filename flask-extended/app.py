from flask import Flask, render_template, abort, request, flash
from movie_ratings import ratings, directors
from models.init_db import db
from models.movie import Movie
from models.tag import MovieTag
import sys

app = Flask(__name__)
app.secret_key = b"fgfxnfykxjxtjr"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
db.init_app(app)

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/details/<int:movie_id>")
def details_page(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    return render_template("details.html", movie=movie)


@app.get("/add")
def add_movie():
    return render_template("add.html", directors=directors)


@app.post("/add")
def add_movie_form():
    movie_name = request.form["title"]
    movies_with_title = db.session.execute(
        db.select(Movie).where(
                Movie.name == movie_name
            )
        ).scalar()
    if movies_with_title:
        flash("Ten film jest już w bazie danych")
        return render_template("add.html", directors=directors)
    cat_death = "cat_death" in request.form
    violence = "violence" in request.form
    loud_noises = "loud_noises" in request.form
    jump_scares = "jump_scares" in request.form
    tag = request.form["tag"]

    movie_object = Movie(
        name = movie_name,
        cat_death = cat_death,
        violence = violence,
        loud_noises = loud_noises,
        jump_scares = jump_scares
    )
    db.session.add(movie_object)
    db.session.commit()

    # Dodawnanie tagów do filmów
    for i in tag.split(","):
        if len(i) == "":
            continue
        movie_tag_object = MovieTag(
            tag_name = i,
            movie_id = movie_object.id
        )
        db.session.add(movie_tag_object)
    db.session.commit()

    return details_page(movie_object.id)


@app.get("/search")
def search_movies():
    query = request.args.get("query", "").lower()
    results = db.session.execute(
        db.select(Movie).where(
            Movie.name.contains(query)
        )
    ).scalars()
    return render_template("search.html", results=results)

@app.get("/tag")
def movie_tag():
    query = request.args.get("query", "").lower()
    results = db.session.execute(
        db.select(MovieTag.movie).where(
            MovieTag.tag_name == query
        )
    ).scalars()
    return render_template("search.html", results=results)

@app.get("/director/<int:director_id>")
def director_page(director_id):
    director = directors.get(director_id)
    if not director:
        abort(404)
    movies = [
        movie for movie in ratings.values() if movie.get("Director") == director_id
    ]
    return render_template("director.html", director=director, movies=movies)


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "setup":
        with app.app_context():
            db.create_all()
            for movie in ratings.values():
                movie_object = Movie(
                    name=movie['title'],
                    cat_death=movie['cat_death'],
                    violence=movie['violence'],
                    loud_noises=movie['loud_noises'],
                    jump_scares=movie['jump_scares']
                )
                db.session.add(movie_object)
            db.session.commit()
    elif command == "serve":
        app.run(debug=True)
