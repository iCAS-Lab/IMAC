import keras
from keras.datasets import mnist
from keras.layers import Conv2D, Dense, MaxPool2D, Dropout, Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.models import Sequential
from keras import backend as K

class LeNet5:
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()
        inputShape = (height, width, depth)

        model.add(Conv2D(6, kernel_size=(5,5),
                            padding="same", activation="relu", 
                            input_shape=inputShape ))
        model.add(MaxPool2D(pool_size=(2,2)))
        model.add(Conv2D(16, kernel_size=(5,5), 
                            padding="valid", activation="relu"))
        model.add(MaxPool2D(pool_size=(2,2)))
        model.add(Flatten())
        model.add(Dense(120, activation="relu"))
        model.add(Dense(84, activation="relu"))
        model.add(Dense(10, activation="softmax"))

        return model