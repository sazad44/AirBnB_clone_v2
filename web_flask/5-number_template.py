#!/usr/bin/python3
"""Python script to start a flask web application"""
from flask import Flask, render_template

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


@app.route("/python", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Python function to output Python followed by input value"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """Number function displays n if it is an integer only"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Number Template function provides support for responding with HTML"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
