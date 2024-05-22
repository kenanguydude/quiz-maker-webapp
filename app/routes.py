from flask import Flask, render_template, request, make_response
import sqlite3

app = Flask(__name__)

# connect to database
conn = sqlite3.connect('database/quiz.db')
cur = conn.cursor()

# routes


@app.route("/")
def home():
    """The page it brings you to when you open the website."""
    return render_template("home.html")


@app.route("/quizzes")
def quizzes():
    """Where you can take and make a quiz."""
    return render_template("quizzes.html")


if __name__ == "__main__":
    app.run(debug=True)
