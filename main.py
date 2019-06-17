from data.data_loader import DataLoader
from convolution_functions import convolution_layer, max_pool_layer
from fully_conected_layer import fully_connected_layer
from training import cost_function, cost_minimalization
import tensorflow as tf
import numpy as np

#wczytywanie danych
classes_path = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_meta.mat'
training_annotations  = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_train_annos.mat' 
training_images = r'C:\Users\tomi8\Desktop\Dataset\cars_train'

training_data_loader = DataLoader(classes_path,training_annotations,training_images)
dataset=training_data_loader.getDataset()
#dataset - zawiera pary (zdjecie, id klasy)
print(dataset)

#graf pobierajacy batch zdjec z datasetu
batch_size = 25 # 128
iterator = dataset.repeat().batch(batch_size).make_initializable_iterator()
data_batch = iterator.get_next()

# parameters
display_step = 20

#network hyperparameters -> beda zmieniane w procesie "doskonalenia" sieci

learning_rate = 0.001
training_iters = 100

dropout = 0.75 # Dropout, probability to keep units


classes_number = 2 #196
image_size = 128 #????? musimy wybrac rozmiar zdjec 

x = tf.placeholder("float", [None, image_size,image_size,1])
y = tf.placeholder("float", [None, classes_number])

x = tf.reshape(x, [-1, image_size, image_size, 1])

def map_predictions_to_classification(predictions):
        return tf.one_hot(tf.argmax(predictions,1),depth=2)

# Constructing model
def cnn_model(input):
        first_layer = convolution_layer(input,1,[2,2],1)
        print(first_layer)
        pooled_first_layer = max_pool_layer(first_layer,[2,2],[1,2,2,1])
        print(pooled_first_layer)
        pooled_layer_shape = pooled_first_layer.get_shape()
        predictions = fully_connected_layer(pooled_first_layer, [64,64,1])
        print(predictions)
        classification = map_predictions_to_classification(predictions)        
        print(classification)
        return predictions

predictions = cnn_model(x)
# loss and optimizer
cost = cost_function(predictions, y)
optimizer = cost_minimalization(cost, learning_rate)

# Evaluate model
correct_pred = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    sess.run(iterator.initializer)
    step = 1
    batches_count = 2
    currentAccuracy = 0

    for epoch in range(training_iters):
        currentAccuracy = 0
        
        for batch in range(batches_count):
                batch_images, batch_labels = sess.run(data_batch)
                 
                
                sess.run(optimizer, feed_dict={x: batch_images, y:batch_labels })
                if step % display_step == 0:
                        loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_images, y:batch_labels})
                        print("Iter " + str(step*batch_size) + ", Minibatch Loss= " + \
                         "{:.6f}".format(loss) + ", Training Accuracy= " + \
                         "{:.5f}".format(acc))
                step += 1
        print("Optimization finished")
        batch_images, batch_labels = sess.run(data_batch)
        print("Testing Accuracy:", \
        sess.run(accuracy, feed_dict={x: batch_images,
                                      y: batch_labels,
                                     }))