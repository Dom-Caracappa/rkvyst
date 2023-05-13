from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home(name=None):
    return render_template('home.html', name=name)

