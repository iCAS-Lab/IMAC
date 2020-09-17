import keras
import numpy as np
import cv2
import os
from keras.datasets import mnist
import keras.layers as layers
from keras.layers import Conv2D, Dense, AveragePooling2D, Flatten, Activation
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.models import Sequential
from pynumbers.lenet5 import LeNet5

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#os.environ['CUDA_VISIBLE_DEVICES']='2'

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

y_train=to_categorical(y_train,num_classes=10)
y_test=to_categorical(y_test,num_classes=10)

x_train = np.pad(x_train, ((0,0),(2,2),(2,2), (0,0)), 'constant')
x_test = np.pad(x_test, ((0,0),(2,2),(2,2), (0,0)), 'constant')

print(x_train[0].shape)

model = keras.Sequential()

model.add(layers.Conv2D(filters=6, kernel_size=(5, 5), activation='tanh', input_shape=(32,32,1)))
model.add(layers.AveragePooling2D())

model.add(layers.Conv2D(filters=16, kernel_size=(5, 5), activation='tanh'))
model.add(layers.AveragePooling2D())

model.add(layers.Activation('tanh'))

model.add(layers.Flatten())

model.add(layers.Dense(units=120, activation='tanh'))

model.add(layers.Dense(units=84, activation='tanh'))

model.add(layers.Dense(units=10, activation = 'sigmoid'))

opt = Adam(lr=5e-4)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])
model.summary()

model.fit(x_train,y_train,batch_size=120,epochs=40,validation_data=(x_test, y_test))
model.save('lenet.h5')

