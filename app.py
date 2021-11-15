from imageio import imread
from skimage.transform import resize
from skimage.color import rgb2gray, rgba2rgb
from flask import Flask, render_template, request
import numpy as np
import flask_restful
import re
import base64
import tensorflow as tf


app = Flask(__name__)
api = flask_restful.Api(app)


def parseImg(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b"base64,(.*)", imgData).group(1)
    with open("output.jpg", "wb") as output:
        output.write(base64.decodebytes(imgstr))


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
        img = imread("output.jpg") / np.float32(255)
        img = rgba2rgb(img)
        img = rgb2gray(img)
        img = resize(img, (28, 28))
        img = np.array(img < 0.9).astype(np.float32)
        img = tf.expand_dims(img, 0)
        img = tf.expand_dims(img, -1)

        pred = model.predict(img)
        result = pred.argmax()

        return str(result)


if __name__ == "__main__":
    print("server run")
    model = tf.keras.models.load_model("./model/mnist.h5")
    app.run(host="localhost", port="5000", debug=True)
