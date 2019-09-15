import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD

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
    model.add(Dropout(0.75))
    model.add(Dense(2))
    model.add(Activation('softmax'))

    if weights is not None:
        model.load_weights(weights)

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])
    return model