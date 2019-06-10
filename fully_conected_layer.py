import tensorflow as tf

#ostatnia warstwa sieci neuronowej, korzysta z funkcji aktywacji relu oraz softmax 
# (softmax dletego ze mamy wiele klas obrazow), zwraca y czyli wektor predykcji
def fully_connected_layer(input_data,input_shape):
    flattened = tf.reshape(input_data, [-1, input_shape[0] * input_shape[1] * input_shape[2]])

    weights_1 = tf.Variable(tf.truncated_normal([input_shape[0] * input_shape[1] * input_shape[2], 1000], stddev=0.03))
    biases_1 = tf.Variable(tf.truncated_normal([1000], stddev=0.01))
    dense_layer1 = tf.matmul(flattened, weights_1) + biases_1
    dense_layer1 = tf.nn.relu(dense_layer1)

    weights_2 = tf.Variable(tf.truncated_normal([1000, 2], stddev=0.03), name='wd2')
    biases_2 = tf.Variable(tf.truncated_normal([2], stddev=0.01), name='bd2')
    dense_layer2 = tf.matmul(dense_layer1, weights_2) + biases_2
    y = tf.nn.softmax(dense_layer2)

    return y