import os

import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

from utils.singleton import Singleton

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


class Model(metaclass=Singleton):
    def __init__(self) -> None:
        self.model = self.init_model()
        self.categories = {0: "positive", 1: "negative"}
        self.tokenizer = Tokenizer(num_words=10000)

    def init_model(self):
        if os.path.exists("model.h5"):
            return keras.models.load_model("model.h5")

        model = keras.Sequential(
            [
                keras.layers.Dense(64, activation="relu", input_shape=[10000]),
                keras.layers.Dense(3, activation="softmax"),
                keras.layers.Dense(1, activation='sigmoid')
            ]
        )
        model.compile(
            optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
        )
        model.save("model.h5")

        return model

    def predict(self, comment):
        self.tokenizer.fit_on_texts([comment])
        comment_vec = self.tokenizer.texts_to_matrix([comment])
        pred = self.model.predict(comment_vec)

        pred_index = np.argmax(pred)

        if pred_index in self.categories:
            return self.categories[np.argmax(pred)]
        
        return "unknow"
    

    def train(self, comment, category):
        X_train = []
        y_train = []
        category_id = list(self.categories.keys())[list(self.categories.values()).index(category)]

        y_train.append(category_id)
        X_train.append(comment)

        X_train_vec = self.tokenizer.texts_to_matrix(X_train)
        y_train_cat = np.asarray(y_train)

        self.model.fit(X_train_vec, y_train_cat, epochs=1)
        self.model.save("model.h5")



model = Model()
