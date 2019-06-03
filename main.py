from data.data_loader import DataLoader
from convolution_functions import convolution_layer, max_pool_layer
from fully_conected_layer import fully_connected_layer
from training import cost_function, cost_minimalization
import tensorflow as tf
import numpy as np

#wczytywanie danych
classes_path = r'C:\Users\kubec\Desktop\Dataset\devkit\cars_meta.mat'
training_annotations  = r'C:\Users\kubec\Desktop\Dataset\devkit\cars_train_annos.mat' 
training_images = r'C:\Users\kubec\Desktop\Dataset\cars_train'

training_data_loader = DataLoader(classes_path,training_annotations,training_images)
dataset=training_data_loader.getDataset()
#dataset - zawiera pary (zdjecie, id klasy)


#network hyperparameters -> beda zmieniane w procesie "doskonalenia" sieci

learning_rate = 0.001
training_iters = 10
batch_size = 25 # 128


classes_number = 2 #196
image_size = 192 #????? musimy wybrac rozmiar zdjec 

x = tf.placeholder("float", [None, image_size,image_size,1])
y = tf.placeholder("float", [None, classes_number])

x = tf.reshape(x, [-1, image_size, image_size, 3])

result = convolution_layer(x,3,[2,2],1)
tmp_dataset = []

for element in dataset:
    if element[1] == 13 or element[1] == 2:
        reshaped_image =  tf.reshape(element[0], [1, 28, 28, 3])
        new_elem = [reshaped_image,element[1]]
        tmp_dataset.append(new_elem)

print(len(tmp_dataset))

def map_predictions_to_classification(predictions):
        return tf.one_hot(tf.argmax(predictions,1),depth=2)

first_layer = convolution_layer(tmp_dataset[0][0],3,[2,2],1)
print(first_layer)
pooled_first_layer = max_pool_layer(first_layer,[2,2],[1,2,2,1])
print(pooled_first_layer)
pooled_layer_shape = pooled_first_layer.get_shape()
predictions = fully_connected_layer(pooled_first_layer, [14,14,1])
print(predictions)
classification = map_predictions_to_classification(predictions)        
print(classification)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    
    batches_count = len(tmp_dataset)//batch_size
    currentAccuracy = 0

    for epoch in range(training_iters):
        currentAccuracy = 0
        print(sess.run(classification))
        for batch in range(batches_count):
                data = tmp_dataset[batch * batch_size : (batch+1) * batch_size]