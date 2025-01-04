from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcom into Parking app</h1>"


@app.route('/user/<name>')
def user(name):
    return f"<h1>Welcome, {name}!</h1>"
