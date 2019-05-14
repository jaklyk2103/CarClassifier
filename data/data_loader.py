import pathlib
import scipy.io
import tensorflow as tf


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
        cropped_image=tf.image.crop_to_bounding_box(
            img_tensor, min_y, min_x, max_y, max_x)
        image=tf.image.resize_images(cropped_image, [192, 192])
        image /= 255.0  # normalize to [0,1] range
        return image

    def __read_and_preprocess_image(self,path, annotations):
        img_raw=tf.read_file(path)
        return self.__preprocess_image(img_raw, annotations.min_x,
        annotations.min_y, annotations.max_x, annotations.max_y, 192, 192)

    def getDataset(self):
        classes = scipy.io.loadmat(self.classes_path)
        annotations = scipy.io.loadmat(self.annotations_path,squeeze_me=True)
        images_path = pathlib.Path(self.images_path)

        all_image_paths = list(images_path.glob('*.jpg'))
        all_image_paths = [str(path) for path in all_image_paths]

        image_class_id_list = [item['class'] -1 for item in annotations['annotations']]
        class_id_dataset = tf.data.Dataset.from_tensor_slices(image_class_id_list)


        image_count = len(all_image_paths)
        print("loaded", image_count, "images")

        annotations_list = []
        print(all_image_paths[11])
        images_list = []
        for counter in range(10):
            print(counter)
            current_ann = annotations['annotations'][counter]
            element = ImageAnnotations(current_ann['bbox_x1'], current_ann['bbox_y1'],
            current_ann['bbox_x2'], current_ann['bbox_y2'], current_ann['fname'], current_ann['class'])
            annotations_list.append(element)
            images_list.append(self.__read_and_preprocess_image(all_image_paths[counter],element))
              
        images_datset = tf.data.Dataset.from_tensor_slices(images_list)  
        dataset = tf.data.Dataset.zip((class_id_dataset,class_id_dataset))
        return dataset

        

