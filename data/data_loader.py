import pathlib
import scipy.io
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder
import numpy as np



class ImageAnnotations:
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    name = ''
    classId = 0

    def __init__(self, min_x, min_y, max_x, max_y, name, classId):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.name = name
        self.classId = classId


class DataLoader:
    classes_path = ''
    annotations_path = ''
    images_path = ''

    def __init__(self, classes_path, annotations_path, images_path):
        self.classes_path = classes_path
        self.annotations_path = annotations_path
        self.images_path = images_path

    def __preprocess_image(self,image, min_x, min_y, max_x, max_y, target_width, target_height):
        img_tensor=tf.image.decode_jpeg(image, channels=3)
        cropped_x = max_x - min_x
        cropped_y = max_y - min_y
        cropped_image=tf.image.crop_to_bounding_box(img_tensor, min_y, min_x, cropped_y, cropped_x)
        image=tf.image.resize_images(cropped_image, [28, 28])
        image /= 255.0  # normalize to [0,1] range
        return image

    def __read_and_preprocess_image(self,path, annotations):
        img_raw=tf.read_file(path)
        return self.__preprocess_image(img_raw, annotations.min_x,
        annotations.min_y, annotations.max_x, annotations.max_y, 28, 28)

    def getDataset(self):
        classes = scipy.io.loadmat(self.classes_path)
        annotations = scipy.io.loadmat(self.annotations_path,squeeze_me=True)
        images_path = pathlib.Path(self.images_path)

        all_image_paths = list(images_path.glob('*.jpg'))
        all_image_paths = [str(path) for path in all_image_paths]

        #image_class_id_list = [item['class'] -1 for item in annotations['annotations']]
        image_class_id_list = []


        image_count = len(all_image_paths)
        print("loaded", image_count, "images")

        annotations_list = []
        print(all_image_paths[11])
        images_list = []
        for counter in range(8144):
            current_ann = annotations['annotations'][counter]
            element = ImageAnnotations(current_ann['bbox_x1'], current_ann['bbox_y1'],
            current_ann['bbox_x2'], current_ann['bbox_y2'], current_ann['fname'], current_ann['class'])
            if element.classId == 2 or element.classId == 3:
                annotations_list.append(element)
                images_list.append(self.__read_and_preprocess_image(all_image_paths[counter],element))
                image_class_id_list.append(element.classId)

        onehotencoder = OneHotEncoder(categorical_features = [0])
        class_id_array = np.asarray(image_class_id_list).reshape(-1,1)
        encoded_labels = onehotencoder.fit_transform(class_id_array).toarray()      
        
        
        return tf.data.Dataset.from_tensor_slices((images_list,encoded_labels))

        

