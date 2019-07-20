# -*- coding: utf-8 -*-
"""20151529.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13skYs10BPT39xmuRrrk58D-S1N0eUE6K

# Import modules
"""

import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.utils.vis_utils import model_to_dot
from IPython.display import SVG
# %matplotlib inline
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns

"""# Tuning parameters"""

epochs = 35
learning_rate=0.0285 #Parameter, Layer, 등을 바꿔본다든지. Keras.io/examples/cifar10_cnn/ 의 문서를 잘 읽어보고 비슷하게 따라하면 된다. 프로젝트는 코드가 비슷할테니, '분석'을 얼마만큼 잘 할 것인지. 코드는 정확성이 75프로 이상이면 만점. 보고서에서 모델에 대한 이해를 얼마만큼했느냐!

batch_size = 32
num_classes = 10

"""# Data

## Plot image
"""

def plot_images(x, y_true, y_pred=None, size=(5, 5)):
    assert len(x) == len(y_true) == size[0] * size[1]
    
    fig, axes = plt.subplots(size[0], size[1])
    fig.subplots_adjust(hspace=0.5, wspace=0.1)

    for i, ax in enumerate(axes.flat):
        if x[i].shape[-1] == 1:
          ax.imshow(x[i].reshape(x[i].shape[0], x[i].shape[1]))
        else:
          ax.imshow(x[i])

        if y_pred is None:
            xlabel = "True: {0}".format(y_true[i].argmax())
        else:
            xlabel = "True: {0}, Pred: {1}".format(y_true[i].argmax(), 
                                                   y_pred[i].argmax())

        ax.set_xlabel(xlabel)
        
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()

"""## Load dataset"""

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

"""## Reshaping the data"""

if len(x_train.shape) < 4:
  x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
  x_test = x_test.reshape(x_test.shape[0], x_train.shape[1], x_train.shape[2], 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

"""## Applying One hot encoding for the data"""

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""## Show data"""

plot_images(x_train[:25], y_train[:25])

"""# Creating the DNN model"""

model = Sequential()

"""## Adding layers to the model"""

model.add(Conv2D(48, (3, 3), padding='same',input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(48, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.4))

model.add(Conv2D(48, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(48, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.4))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

"""## Visualization the model"""

SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

"""## Optimizer"""

#optimizer = keras.optimizers.Adam(lr=learning_rate, beta_1=0.9, beta_2=0.999) #Lr = 0.001
optimizer = keras.optimizers.SGD(lr=learning_rate) #, Lr = 0.00285

"""## Compiling the model"""

model.compile(loss=keras.losses.categorical_crossentropy, 
              optimizer=optimizer, 
              metrics=['accuracy'])

"""## Training the model"""

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

"""## Evaulating the model"""

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""## Prediction the model"""

y_pred = model.predict(x_test)

plot_images(x=x_test[:25], y_true=y_test[:25], y_pred=y_pred[:25])

y_result = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
sns.heatmap(pd.DataFrame(y_result, range(10), range(10)), annot=True, fmt='g')