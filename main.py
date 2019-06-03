from data.data_loader import DataLoader
from convolution_functions import convolution_layer, max_pool_layer
from fully_conected_layer import fully_connected_layer
from training import cost_function, cost_minimalization
import tensorflow as tf
import numpy as np


def map_image_class_to_array(image_class_id, number_of_classes):
    result_array = []
    for image_class in range(number_of_classes):
        if image_class_id != image_class:
            result_array.append(0)
        else:
            result_array.append(1)
    return result_array

#wczytywanie danych
classes_path = r'C:\Users\kuba\Desktop\Dataset\devkit\cars_meta.mat'
training_annotations  = r'C:\Users\kuba\Desktop\Dataset\devkit\cars_train_annos.mat' 
training_images = r'C:\Users\kuba\Desktop\Dataset\cars_train'

training_data_loader = DataLoader(classes_path,training_annotations,training_images)
dataset=training_data_loader.getDataset()
#dataset - zawiera pary (zdjecie, id klasy)

# parameters
display_step = 10

#network hyperparameters -> beda zmieniane w procesie "doskonalenia" sieci

learning_rate = 0.001
training_iters = 10
batch_size = 25 # 128
dropout = 0.75 # Dropout, probability to keep units


classes_number = 2 #196
image_size = 192 #????? musimy wybrac rozmiar zdjec 

x = tf.placeholder("float", [None, image_size,image_size,1])
y = tf.placeholder("float", [None, classes_number])

x = tf.reshape(x, [-1, image_size, image_size, 3])

result = convolution_layer(x,3,[2,2],1)
tmp_dataset = []

for element in dataset:
    if element[1] == 0 or element[1] == 1:
        reshaped_image =  tf.reshape(element[0], [1, 28, 28, 3])
        image_class_id_array = map_image_class_to_array(element[1], classes_number)
        print('element[1]:')
        print(image_class_id_array)
        new_elem = [reshaped_image,image_class_id_array]
        tmp_dataset.append(new_elem)

print(len(tmp_dataset))

def map_predictions_to_classification(predictions):
        return tf.one_hot(tf.argmax(predictions,1),depth=2)

# Constructing model
first_layer = convolution_layer(tmp_dataset[0][0],3,[2,2],1)
print(first_layer)
pooled_first_layer = max_pool_layer(first_layer,[2,2],[1,2,2,1])
print(pooled_first_layer)
pooled_layer_shape = pooled_first_layer.get_shape()
predictions = fully_connected_layer(pooled_first_layer, [14,14,1])
print(predictions)
classification = map_predictions_to_classification(predictions)        
print(classification)

# loss and optimizer
cost = cost_function(classification, y)
optimizer = cost_minimalization(cost, learning_rate)

# Evaluate model
correct_pred = tf.equal(tf.argmax(classification, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 1
    batches_count = len(tmp_dataset)//batch_size
    currentAccuracy = 0

    for epoch in range(training_iters):
        currentAccuracy = 0
        print(sess.run(classification))
        for batch in range(batches_count):
                data = tmp_dataset[batch * batch_size : (batch+1) * batch_size]
                data_x = map(lambda x: x[0], data)
                data_y = map(lambda x: x[1], data)
                sess.run(optimizer, feed_fict={x: data_x, y:data_y, keep_prob: dropout })
                if step % display_step == 0:
                    loss, acc = sess.run([cost, accuracy], feed_dict={x:batch_x, y: batch_y, keep_prob: 1.})
                    print("Iter " + str(step*batch_size) + ", Minibatch Loss= " + \
                        "{:.6f}".format(loss) + ", Training Accuracy= " + \
                        "{:.5f}".format(acc))
                step += 1
        print("Optimization finished")
