from flask import Flask, render_template, request
import flask_restful
import tensorflow as tf
import numpy as np

app = Flask(__name__)
api = flask_restful.Api(app)


@app.route("/")
def index():
    title = "Serve Test"
    return render_template("index.html", title=title)


@app.route("/letter", methods=["POST"])
def letter():
    if request.method == "POST":
        letter = request.form
        return letter


if __name__ == "__main__":
    print("server run")
    app.run(host="localhost", port="5000", debug=True)
