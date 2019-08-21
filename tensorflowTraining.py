import pathlib
import scipy.io
import IPython.display as display
import tensorflow as tf

# bede robił duzo komentarzy, żeby się w tym wszystkim nie pogubić

# Zaczynam od proby wczytania naszych danych testowych a nastepnie zrobienia z nich datasetu.
# niestety niejest to takie proste jak w tutorialach poniewaz to nie jest gotowy dataset z frameworka

# informacje o zdjeciach znajduja sie w plikach matlaba (folder devkit), na szczescie jest biblioteka ktora pozwala na ich otwarcie

classes = scipy.io.loadmat(r'C:\Users\Kuba\Desktop\Dataset\devkit\cars_meta.mat', squeeze_me=True)
test = scipy.io.loadmat(r'C:\Users\Kuba\Desktop\Dataset\devkit\cars_train_annos.mat', squeeze_me=True)
trainingImagesPath = pathlib.Path(r'C:\Users\Kuba\Desktop\Dataset\cars_train')

all_image_paths = list(trainingImagesPath.glob('*.jpg'))
all_image_paths = [str(path) for path in all_image_paths]

image_count = len(all_image_paths)

print(image_count)

classNames = classes['class_names']

imagesClassIdList = [item['class'] - 1 for item in test['annotations']]

# test -> zdjecie powinno być zgodne z nazwa klasy
print(all_image_paths[2])
print(classNames[imagesClassIdList[2]])

# wczytywanie zdjecia do tensora (macierzy) -> jak na JA :P
img_raw = tf.read_file(all_image_paths[2])

img_tensor = tf.image.decode_jpeg(img_raw, channels=3)

# przycianie obrazka -> kazdy opis naszego obrazu ma "bounding boxy" dp ktorych nalezy obciac
# obrazy
cropped_image = tf.image.crop_to_bounding_box(img_tensor, 2, 2, 100, 100)

# testowy zapis
saveImage = tf.image.encode_jpeg(cropped_image)
writer = tf.write_file('test.jpg', saveImage)


print(img_tensor.shape)

# wszystko fajnie ale sie nie wykonalo
# tu jest takie ala lazy loading dla tensorowych operacji, read_file oraz
# decode_jpeg sie nie wykonaly, dopiero jak zadeklaruje i uruchomie sesje to sie to wykona


with tf.Session() as sess:
    img = sess.run(img_tensor)
    img2 = sess.run(cropped_image)
    sess.run(writer)
    print(img.shape)
    print(img2.shape)

# tu juz wszystko poszlo zgodnie z planem