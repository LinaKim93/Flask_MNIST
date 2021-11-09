from imageio import imread
from skimage.transform import resize
from skimage.color import rgb2gray
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import flask_restful
import json
import re
import base64
import tensorflow as tf

import sys
import os

sys.path.append(os.path.abspath("./model"))

app = Flask(__name__)
api = flask_restful.Api(app)


def parseImg(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b"base64,(.*)", imgData).group(1)
    with open("output.jpg", "wb") as output:
        output.write(base64.decodebytes(imgstr))


def testImg():
    # img = imread("output.jpg") / 255
    img = imread("test.jpg") / 255
    print(img.shape)
    img = rgb2gray(img)
    img = resize(img, (1, 28, 28, 1))
    model = tf.keras.models.load_model("./model/mnist.h5")

    pred = model.predict(img)
    print(pred.argmax())


@app.route("/")
def index():
    title = "Serve Test"
    return render_template("index.html", title=title)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        data = request.get_data()
        parseImg(data)
        return "POST"

    if request.method == "GET":
        img = imread("output.jpg") / 255
        img = rgb2gray(img)
        img = resize(img, (1, 28, 28, 1))

        model = tf.keras.models.load_model("./model/mnist.h5")

        pred = model.predict(img)
        print(pred.argmax())

        result = pred.argmax()

        return str(result)


if __name__ == "__main__":
    print("server run")
    testImg()
    # app.run(host="localhost", port="5000", debug=True)
