#!/usr/bin/python3
"""Python script to start a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello HBNB function to respond to index requests"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Hello HBNB function to respond to hbnb requests"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """C function to output C followed by input value"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
