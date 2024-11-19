from flask import Flask, render_template
from movie_ratings import _ratings

app = Flask(__name__)

@app.get('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)