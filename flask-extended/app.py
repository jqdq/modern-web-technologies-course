from flask import Flask, render_template, abort, request, redirect, url_for
from movie_ratings import ratings

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/movies/<name>")
def movie_details(name):
    movie = ratings.get(name)
    if movie is None:
        return abort(404)
    return render_template(
        "details.html", movie=movie, runtime_h=movie["length_seconds"] / 3600
    )


@app.get("/search")
def search_page():
    query = request.args.get("query", "").lower()
    results = []
    for movie in ratings.values():
        if query in movie["title"].lower():
            results.append(movie)
    return render_template("search.html", movies=results, query=query)


@app.get("/add")
def add_movie_page():
    return render_template("add.html")


@app.post("/add")
def add_movie():
    title = request.form["title"]
    rating = float(request.form["rating"])
    description = request.form["description"]
    owner_review = request.form["owner_review"]
    length = int(request.form["length_seconds"])

    cat_death = "cat_death" in request.form
    violence = "violence" in request.form
    loud_noises = "loud_noises" in request.form
    jump_scares = "jump_scares" in request.form

    ratings[title] = {
        "title": title,
        "rating": rating,
        "description": description,
        "owner_review": owner_review,
        "length_seconds": length,
        "cat_death": cat_death,
        "violence": violence,
        "loud_noises": loud_noises,
        "jump_scares": jump_scares,
    }
    return redirect(url_for("movie_details", name=title))


@app.errorhandler(404)
def generic_error(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
