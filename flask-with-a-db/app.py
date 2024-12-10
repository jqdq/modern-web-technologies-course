from flask import Flask, render_template, abort, request, flash
from flask_wtf import CSRFProtect
from auth import bp, login_required
from movie_ratings import ratings

import sqlite3

app = Flask(__name__)
app.secret_key = "cyvgubhijnomkpohgifcxf"
csrf = CSRFProtect(app)

app.register_blueprint(bp)

@app.get('/')
def home():
    return render_template("index.html")

@app.get("/movies/<title>")
def movie_site(title):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Movies WHERE title=(?)", (title,))
    movie = cursor.fetchone()
    db.close()
    if movie is None:
        abort(404)
    movie = {
        "title": movie[0],
        "cat_death": movie[1],
        "violence": movie[2],
        "loud_noises": movie[3],
        "jump_scares": movie[4]
    }
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
    cat_death = int(request.form.get("cat_death") == "on")
    violence = int(request.form.get("violence") == "on")
    loud_noises = int(request.form.get("loud_noises") == "on")
    jump_scares = int(request.form.get("jump_scares") == "on")

    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM Movies WHERE title=(?)", (title,))
    movie = cursor.fetchone()

    if movie[0] != 0:
        return render_template("add.html", error="Movie already exists in the database")

    cursor.execute("INSERT INTO Movies (title, cat_death, violence, loud_noises, jump_scares) VALUES (?, ?, ?, ?, ?)", (title, cat_death, violence, loud_noises, jump_scares))
    db.commit()
    db.close()

    return render_template("add.html", error=f"Movie '{title}' added successfully")

if __name__ == '__main__':
    app.run(debug=True)