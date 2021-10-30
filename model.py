import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.models import Model

(
    (train_data, train_label),
    (test_data, test_label),
) = tf.keras.datasets.mnist.load_data()

train_data = train_data / np.float32(255)
train_data = train_data.reshape(60000, 28, 28, 1)

test_data = test_data / np.float32(255)
test_data = test_data.reshape(-1, 28, 28, 1)

print(train_data.shape, test_data.shape)

inputs = Input(shape=(28, 28, 1))
x = Conv2D(32, (5, 5), padding="same", activation="relu")(inputs)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (5, 5), activation="relu")(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (5, 5), activation="relu")(x)
x = Flatten()(x)
x = Dense(64, activation="relu")(x)
outputs = Dense(10, activation="softmax")(x)
model = Model(inputs, outputs)

model.summary()

model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
hist = model.fit(
    train_data,
    train_label,
    validation_data=(test_data, test_label),
    batch_size=8,
    epochs=5,
    verbose=1,
)

model.save("mnist.h5")
