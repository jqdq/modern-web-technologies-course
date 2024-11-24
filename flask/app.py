from flask import Flask, render_template, abort, request, flash
from flask_wtf import CSRFProtect
from auth import bp, login_required
from movie_ratings import ratings

app = Flask(__name__)

@app.get('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)