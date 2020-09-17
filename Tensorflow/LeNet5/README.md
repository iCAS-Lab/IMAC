# LeNet-5__Keras_MNIST

### Introduction

> Implementation of LeNet-5 using Keras, and MNIST as training datasets. Able to identify handwritten digits

- LeNet-5    https://engmrk.com/lenet-5-a-classic-cnn-architecture/
- Keras      https://keras.io/
- MNIST of Handwritten digits     http://yann.lecun.com/exdb/mnist/

If you want to read codes to implement LeNet-5, please go [**here**]( https://colab.research.google.com/drive/1PuGJGDzPogo7e1IMaHkEiJn7lNMyGDmY)

### How?

First make sure you have set up the environment

```
- pyhon
  - cv2
  - h5py
- TensorFlow
- Keras
```

Then run `python start.py`

If you are a lazy guy just like me, you can convert it into a `.exe` file using [pyinstaller](https://github.com/pyinstaller/pyinstaller)

OR

you can just run `train.py` to train your netral network

run `classify.py` to identify the number in `test.png`

### Notes

If you want to substitude `test.png`

Make sure it is `28*28` in pixel size

A simple way to make one is to use your **mspaint**

For MacOS and Linux users. Well... I believe you can find a substituition

### Acknowledgement

Inspired by https://blog.csdn.net/u014453898/article/details/97680748 and https://juejin.im/post/5d66b6725188257e99442108

For `cv2` functions, I learned them in https://www.kancloud.cn/aollo/aolloopencv/259610

Thanks my senior [@BoAi01](https://github.com/BoAi01) for his guidance and help
