from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f"<h1>Welcome into Parking app</h1>\n<p>Your browser is {user_agent}</p>"


@app.route('/user/<name>')
def user(name):
    return f"<h1>Welcome, {name}!</h1>"
