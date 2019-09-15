import cv2 as cv
import keras.backend as K
import numpy as np
from keras.models import model_from_json
from model import get_full_model
import os
from keras.optimizers import SGD
import tensorflow as tf
import scipy.io

def predict(test_image_number):

    model = get_full_model(0.0001, weights="saved_models/2classes_classifier.h5")

    keras_file = "saved_models/model.h5"

    filename = os.path.join('data/test', '%05d.jpg' % 6892)

    print(filename)

    bgr_img = cv.imread(filename)
    rgb_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGB)
    rgb_img = cv.resize(src=rgb_img, dsize=(224,224))
    rgb_img = np.expand_dims(rgb_img, 0)
   
    preds = model.predict(rgb_img)

    print(preds)
    prob = np.max(preds)

    class_id = np.argmax(preds)
    print(class_id)
    
    classesList = [line.rstrip('\n') for line in open('Output.txt')]
    print(classesList[class_id])

if __name__ == '__main__':
    predict(0)