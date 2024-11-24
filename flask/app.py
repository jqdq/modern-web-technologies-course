from flask import Flask, render_template, abort, request, flash
from flask_wtf import CSRFProtect
from auth import bp, login_required
from movie_ratings import ratings

app = Flask(__name__)
app.secret_key = "[add this]"
csrf = CSRFProtect(app)

app.register_blueprint(bp)

@app.get('/')
def home():
    return render_template("index.html")

@app.get("/movies/<title>")
def movie_site(title):
    movie = ratings.get(title)
    if movie is None:
        abort(404)
    return render_template("details.html", movie=movie)

@app.get("/search")
def search():
    query = request.args.get("query")
    if query is None:
        abort(400)

    movie_titles = []
    for movie_title in ratings:
        if query.lower() in movie_title.lower():
            movie_titles.append(movie_title)

    return render_template("search.html", query=query, movies=movie_titles)

# Adding new movies to the DB

@app.get("/add")
@login_required
def get_add_movie_form():
    return render_template("add.html")

@app.post("/add")
@login_required
def add_movie():
    title = request.form.get("title")
    cat_death = request.form.get("cat_death") == "on"
    violence = request.form.get("violence") == "on"
    loud_noises = request.form.get("loud_noises") == "on"
    jump_scares = request.form.get("jump_scares") == "on"

    if title in ratings:
        return render_template("add.html", error="Movie already exists in the database")

    ratings[title] = {
        "title": title,
        "cat_death": cat_death,
        "violence": violence,
        "loud_noises": loud_noises,
        "jump_scares": jump_scares
    }

    return render_template("add.html", error=f"Movie '{title}' added successfully")

if __name__ == '__main__':
    app.run(debug=True)