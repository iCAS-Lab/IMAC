import keras
import cv2
import os
import numpy as np
import keras.backend as K
import tensorflow as tf
from keras.models import load_model
from keras.datasets import mnist
from keras import Model
from keras.utils import to_categorical
from numpy import savetxt

os.environ['CUDA_VISIBLE_DEVICES']='2'

load_model = load_model("./lenet.h5")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)

x_train = np.pad(x_train, ((0,0),(2,2),(2,2), (0,0)), 'constant')
x_test = np.pad(x_test, ((0,0),(2,2),(2,2), (0,0)), 'constant')

y_train=to_categorical(y_train,num_classes=10)
y_test=to_categorical(y_test,num_classes=10)
print("Using loaded model to predict...")
model_output = load_model.get_layer("flatten").output
m = Model(inputs=load_model.input, outputs=model_output)
m.summary()

img = x_test[0]
img = img.reshape(-1, 32, 32, 1)
flatten_out = m.predict(img)

print("Done")