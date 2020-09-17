import keras
import cv2
import numpy as np
import keras.backend as K
import tensorflow as tf
from keras.models import load_model
from keras.datasets import mnist
from keras import Model
from keras.utils import to_categorical
from numpy import savetxt

numSamples = 10000

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
flatten_layer_data = a = np.zeros((numSamples,400))
print(flatten_layer_data.shape)
for num in range(0,numSamples):
    img = x_test[num]
    img = img.reshape(-1, 32, 32, 1)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    flatten_out = m.predict(img)
    flatten_layer_data[num] = flatten_out

savetxt('train_labels.csv', y_train, delimiter=',')
savetxt('test_data.csv', flatten_layer_data, delimiter=',')