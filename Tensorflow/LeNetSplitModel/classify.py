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

numSamples = 60000

load_model = load_model("./lenet.h5")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)
y_train=to_categorical(y_train,num_classes=10)
y_test=to_categorical(y_test,num_classes=10)
print("Using loaded model to predict...")
model_output = load_model.get_layer("flatten").output
m = Model(inputs=load_model.input, outputs=model_output)
flatten_layer_data = a = np.zeros((numSamples,400))
print(flatten_layer_data.shape)
for num in range(0,numSamples):
    #print(np.argmax(y_test[num]))
    img = x_train[num]
    img = img.reshape(-1, 28, 28, 1)
    #img = cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
    #output=img.copy()
    #img = img.astype('float32')
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    predicted = load_model.predict(img)
    #print(predicted)
    predicted = np.argmax(predicted)
    flatten_out = m.predict(img)
    flatten_layer_data[num] = flatten_out
    #print(flatten_out.shape)
    #savetxt('data.csv', flaten_layer_data, delimiter=',')
    #print(predicted)

savetxt('train_labels.csv', y_train, delimiter=',')
savetxt('train_data.csv', flatten_layer_data, delimiter=',')