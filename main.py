from data.data_loader import DataLoader
from convolution_functions import convolution_layer
import tensorflow as tf
import numpy as np

#wczytywanie danych
classes_path = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_meta.mat'
training_annotations  = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_train_annos.mat' 
training_images = r'C:\Users\tomi8\Desktop\Dataset\cars_train'

training_data_loader = DataLoader(classes_path,training_annotations,training_images)
dataset=training_data_loader.getDataset()
#dataset - zawiera pary (zdjecie, id klasy)


#network hyperparameters -> beda zmieniane w procesie "doskonalenia" sieci

learning_rate = 0.001
training_iters = 200000
batch_size = 128

classes_number = 196
input_number = 192 #????? musimy wybrac rozmiar zdjec 

x = tf.placeholder("float", [None, 192,192,1])
y = tf.placeholder("float", [None, classes_number])

x = tf.reshape(x, [-1, 192, 192, 3])

result = convolution_layer(x,3,[2,2],1)
tmp_dataset = []

for element in dataset:
    if element[1] == 1 or element[1] == 2:
        tmp_dataset.append(element)

print(len(tmp_dataset))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    
    
    
 