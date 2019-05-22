from data.data_loader import DataLoader
import tensorflow as tf

#wczytywanie danych
classes_path = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_meta.mat'
training_annotations  = r'C:\Users\tomi8\Desktop\Dataset\devkit\cars_train_annos.mat' 
training_images = r'C:\Users\tomi8\Desktop\Dataset\cars_train'

training_data_loader = DataLoader(classes_path,training_annotations,training_images)
dataset=training_data_loader.getDataset()
#dataset - zawiera pary (zdjecie, id klasy)
iter = dataset.make_one_shot_iterator()
el = iter.get_next()
print(el)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
 