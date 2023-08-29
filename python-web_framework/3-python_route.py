"""Simple script that starts a flask web application
listens on 0.0.0.0, port 5000
Routes:
    /: display Hello HBNB!
    /hbnb: display HBNB
    /c/<text>: handles variables"""

from flask import Flask

app = Flask(__name__)


# decorator to register a route with the app, '/' is the root path of our web application and will be used
@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
@app.route("/c/", defaults={"text": "is cool"})
def get_text(text):
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/<text>")
@app.route("/python/", defaults={"text": "is cool"})
def get_python_text(text):
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


if __name__ == "__main__":
    app.run(debug=True)
