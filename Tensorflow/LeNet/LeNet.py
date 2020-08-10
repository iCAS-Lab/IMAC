import tensorflow as tf
import numpy as np
from numpy import genfromtxt
import keras
import keras.backend as K
from keras.layers import Dense
from keras.callbacks import Callback
from keras.layers import Conv2D
from keras.layers import Flatten
from keras.layers import AveragePooling2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import GlobalAveragePooling2D
from keras.layers import BatchNormalization
from keras import Input, Model, Sequential
from keras.utils import to_categorical
from sklearn.metrics import precision_recall_fscore_support
from keras.optimizers import adam
from keras.optimizers import Adadelta
import os

from keras.callbacks import Callback
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
import datetime

dirName = "Container3"

dataDirectory = "/Users/brendan/Documents/USCWorkStudy/SummerViasProject/TrainingData/"

try:  
  os.mkdir(dirName)  
except OSError as error: 
  c=1+1

try:  
  os.mkdir(dirName + "/images")  
except OSError as error: 
  c=1+1

baseName = dirName + "/"

y_train = genfromtxt(dataDirectory + 'disjoint_train_labels.txt', delimiter=',')
y_test = genfromtxt(dataDirectory + 'disjoint_val_labels.txt', delimiter=',')

x_train = genfromtxt(dataDirectory + 'disjoint_train_data.txt', delimiter=',')
x_test = genfromtxt(dataDirectory + 'disjoint_val_data.txt', delimiter=',')
print(len(y_test))
print(len(y_train))

size_test = len(y_test)
size_train = len(y_train)

x_test = x_test.reshape(size_test,54,54,1)
x_train = x_train.reshape(size_train,54,54,1)



num_classes = 3
rows, cols = 54, 54

def predictionToArray(y_pred):
  anArray = []
  for value in  y_pred:
    currentMax = 0
    for i in range(1,len(value)):
      if value[i] > value[currentMax]:
        currentMax = i
    anArray.append(currentMax)
  return anArray

model = Sequential([
  Conv2D(6, kernel_size=(5,5), activation="tanh", input_shape=(54,54,1), padding='same'),
  AveragePooling2D(pool_size=(2,2), strides=2, padding='valid'),
  Conv2D(16, kernel_size=(5,5), activation="tanh", padding='valid'),
  AveragePooling2D(pool_size=(2,2), strides=2, padding='valid'),
  Conv2D(120, kernel_size=(5,5), activation="tanh", padding='valid'),
  Flatten(),
  Dense(84, activation="tanh"),
  Dense(3,activation="softmax"),
])


opt = Adadelta(lr=1,rho=0.095)

model.summary()

model.compile(
  optimizer = opt,
  loss = "categorical_crossentropy",
  metrics = ["accuracy"],
)

recallList = []
precisionList = []
f1List = []
classAccuracy = []
supportList = []

mostMissed = []
for i in range(0, len(x_test)):
  mostMissed.append(0)

def saveToFile(name, aList, isMultiDim=False):
  print("Saving: " + name)
  with open(name, 'w') as filehandle:
    for value in aList:
      if isMultiDim:
        for i in range(len(value)):
          value2 = value[i]
          filehandle.write('%s' % value2)
          if i<len(value)-1:
            filehandle.write(',')
        filehandle.write('\n')
      else:
        filehandle.write('%s\n' % value)

def getTopNMissed(n):
  if n==-1:
    n=9999
  missed = []
  visited = []
  for _ in range(0,n):
    current = 0
    while current in visited and current < len(mostMissed):
      current = current + 1
    if current >= len(mostMissed):
      return missed
    temp = []
    for j in range(0,len(mostMissed)):
      if mostMissed[j] >= mostMissed[current] and not j in visited:
        current = j
    for j in range(0, len(mostMissed)):
      if not j in visited and mostMissed[j] == mostMissed[current]:
        temp.append(j)
        visited.append(j)
    print(temp)
    missed.append(temp)
  return missed

class IntervalEvaluation(Callback):
    def on_epoch_end(self, epoch, logs={}):
        y_pred = model.predict_proba(x_test, verbose=0)
        y_pred = predictionToArray(y_pred)
        y_true = predictionToArray(y_test)
        score = []
        samples = []
        for i in range(0, num_classes):
          score.append(0)
          samples.append(0)
        for i in range(0,len(y_pred)):
          pred = y_pred[i]
          actual = y_true[i]
          samples[actual] = samples[actual] + 1
          if pred==actual:
            score[actual] = score[actual] + 1
          else:
            mostMissed[i] = mostMissed[i] + 1
        for i in range(0,len(score)):
          score[i] = score[i] / samples[i]
        print(score)
        classAccuracy.append(score)
        saveToFile(baseName + "classAccuracy.txt", classAccuracy, True)

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=250, callbacks=[IntervalEvaluation()])
missed = getTopNMissed(-1)
print(missed)
saveToFile(baseName + "mostMissed.txt", missed, True)
accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

saveToFile(baseName + "accuracy.txt", accuracy)
saveToFile(baseName + "val_accuracy.txt", val_accuracy)
saveToFile(baseName + "missedCount.txt", mostMissed)