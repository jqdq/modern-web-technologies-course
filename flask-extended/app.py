from flask import Flask, render_template, abort, request, flash
from movie_ratings import ratings, directors
from models.init_db import db

app = Flask(__name__)
app.secret_key = b"fgfxnfykxjxtjr"


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/details/<movie_title>")
def details_page(movie_title):
    if movie_title not in ratings:
        abort(404)
    movie = ratings[movie_title]
    return render_template("details.html", movie=movie)


@app.get("/add")
def add_movie():
    return render_template("add.html", directors=directors)


@app.post("/add")
def add_movie_form():
    movie_name = request.form["title"]
    if movie_name in ratings:
        flash("Ten film jest już w bazie danych")
        return render_template("add.html")
    cat_death = "cat_death" in request.form
    violence = "violence" in request.form
    loud_noises = "loud_noises" in request.form
    jump_scares = "jump_scares" in request.form

    ratings[movie_name] = {
        "title": movie_name,
        "cat_death": cat_death,
        "violence": violence,
        "loud_noises": loud_noises,
        "jump_scares": jump_scares,
        "director": int(request.form["director"]),
    }

    return details_page(movie_name)


@app.get("/search")
def search_movies():
    query = request.args.get("query", "").lower()
    results = [movie for movie in ratings.values() if query in movie["title"].lower()]
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
    app.run(debug=True)
