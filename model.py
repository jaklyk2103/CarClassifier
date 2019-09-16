import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
import tensorflow_hub as hub
from keras.applications import MobileNet
from keras.models import Model
from keras.applications import imagenet_utils
from keras.layers import Dense,GlobalAveragePooling2D
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input
import numpy as np

def get_full_model(learningRate, weights = None):
    optimizer = SGD(learningRate)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), strides = (4,4), input_shape =(224,224,3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3),strides = (1,1)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3),strides = (1,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (3, 3), strides =(1, 1)))
    model.add(Activation('relu'))
    model.add(Conv2D(128, (3, 3), strides =(1, 1)))
    model.add(Activation('relu'))
    model.add(Conv2D(128, (3, 3), strides =(1, 1) ))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(320))
    model.add(Activation('sigmoid'))
    model.add(Dropout(0.4))
    model.add(Dense(2))
    model.add(Activation('softmax'))

    if weights is not None:
        model.load_weights(weights)

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])
    return model



def get_mobile_model(learningRate=0, weights = None):
    base_model=MobileNet(weights='imagenet',include_top=False,input_shape=(224,224,3)) #imports the mobilenet model and discards the last 1000 neuron layer.

    x=base_model.output
    x=GlobalAveragePooling2D()(x)
    x=Dense(1024,activation='relu')(x) #we add dense layers so that the model can learn more complex functions and classify for better results.
    x=Dense(1024,activation='relu')(x) #dense layer 2
    x=Dense(512,activation='relu')(x) #dense layer 3
    preds=Dense(4,activation='softmax')(x) #final layer with softmax activation
    model=Model(inputs=base_model.input,outputs=preds)
    for layer in model.layers:
        layer.trainable=False
    model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])
    return model