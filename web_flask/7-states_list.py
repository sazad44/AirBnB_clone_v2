#!/usr/bin/python3
"""Python script starts Flask web application for requests"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tearDown(error):
    """Tear down process when app stops running"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Lists states in database"""
    return render_template("7-states_list.html",
                           state_list=storage.all("State"))


if __name__ == "__main__":
    storage.close()
    app.run(host='0.0.0.0', port=5000)
