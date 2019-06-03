import tensorflow as tf

#cost function - funkcja obliczajaca dokladnosc (skutecznosc) sieci dla kazdej kolejnej predykcji
#im wartosc mniejsza, tym lepsze dopasowanie


def cost_function(predicted_output,expected_output):
    cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(logits=predicted_output, labels=expected_output))
    return cross_entropy

def cost_minimalization(cost,learning_rate):
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)