"""Simple script that starts a flask web application
listens on 0.0.0.0, port 5000
Routes:
    /: display Hello HBNB!"""

from flask import Flask

app = Flask(__name__)


# decorator to register a route with the app, '/' is the root path of our web application and will be used
@app.route("/")
def hello_world():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
