import tensorflow as tf

#funkcja convolution_layer przetwarza obraz zadanym filtrem konwolucyjnym przy uzyciu funkcji conv2d
#bedziemy mieć kilka takich warstw, mozliwe ze z roznymi parametrami, np z rozna wielkoscia filtrow
def convolution_layer(input_data,num_of_channels,filter_shape,filters_number):
    #parametr W funkci conv2d
    
    weights = tf.Variable(tf.truncated_normal([filter_shape[0], filter_shape[1], num_of_channels,filters_number], stddev=0.5))
    out_layer = tf.nn.conv2d(input_data, weights, [1, 1, 1, 1], padding='SAME')
    bias = tf.truncated_normal([filters_number])
    out_layer += bias
    out_layer = tf.nn.relu(out_layer)

    return out_layer
#funkcja max pool zmniejsza rozmiar obrazu stosujac max_pooling
def max_pool_layer(input_data,window_size,strides):
    ksize = [1,window_size[0],window_size[1],1]
    out_layer = tf.nn.max_pool(input_data, ksize=ksize, strides=strides, 
                               padding='SAME')

    