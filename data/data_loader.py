import tarfile
import scipy.io
import numpy as np
import os
import cv2 as cv
import shutil
import random
from console_progressbar import ProgressBar




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





    

def preprocess_image(image, min_x, min_y, max_x, max_y, target_width, target_height):
        
    height, width = image.shape[:2]
    margin = 16
        
    x1 = max(0, min_x - margin)
    y1 = max(0, min_y - margin)
    x2 = min(max_x + margin, width)
    y2 = min(max_y + margin, height)
        
    cropped = image[y1:y2, x1:x2]
    resized = cv.resize(src=cropped, dsize=(target_height, target_width))
        
    return resized

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def save_preprocessed_image(src_path,dst_path, annotations):
    image_raw = cv.imread(src_path)
    image_grey = cv.cvtColor(image_raw, cv.COLOR_BGR2GRAY)
    image = preprocess_image(image_grey, annotations.min_x,
    annotations.min_y, annotations.max_x, annotations.max_y, 224, 224)
    cv.imwrite(dst_path, image)

def prepare_train_dataset(classes_path,annotations_path,images_path,desired_classes=None):
    classes = scipy.io.loadmat(classes_path)
    annotations = scipy.io.loadmat(annotations_path,squeeze_me=True)
    print("number of images: ",len(annotations['annotations']))

    pb = ProgressBar(total=100, prefix='Processing train images...', suffix='', decimals=1, length=20, fill='=')

    train_dataset_ratio = 0.8
    validation_dataset_ratio = 0.2
    image_count = len(annotations['annotations'])

    train_images_number = int(round(image_count * train_dataset_ratio))
    train_images_ids = random.sample(range(image_count), train_images_number)

    class_names =classes['class_names']
    class_names = np.transpose(class_names)
    
    output_file= open("Output.txt","w+")
    
    for id in desired_classes:
        output_file.write(class_names[id-1][0][0] + '\n')
        
    output_file.close()
    for counter in range(image_count):
        current_ann = annotations['annotations'][counter]
        element = ImageAnnotations(current_ann['bbox_x1'], current_ann['bbox_y1'],
        current_ann['bbox_x2'], current_ann['bbox_y2'], current_ann['fname'], current_ann['class'])
           
        src_path = os.path.join(images_path, element.name)
        if counter in train_images_ids:
            dst_folder = 'data/train'
        else:
            dst_folder = 'data/valid'

        dst_path = os.path.join(dst_folder, str(element.classId))
        
        pb.print_progress_bar((counter + 1) * 100 / image_count)

        if desired_classes is None or element.classId in desired_classes:
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            dst_path = os.path.join(dst_path, element.name)
            save_preprocessed_image(src_path,dst_path,element)
        
    
if __name__ == '__main__':

    print('Extracting cars_train.tgz...')
    if not os.path.exists('data\Dataset\cars_train'):
       with tarfile.open('data\Dataset\cars_train.tgz', "r:gz") as tar:
           tar.extractall()


    print('Extracting car_devkit.tgz...')
    if not os.path.exists('data\devkit'):
       with tarfile.open('data\car_devkit.tgz', "r:gz") as tar:
              tar.extractall()

    classes_path = 'data\devkit\cars_meta.mat'
    training_annotations  ='data\devkit\cars_train_annos.mat' 
    training_images = 'data\Dataset\cars_train'


    cars_meta = scipy.io.loadmat(classes_path)
    class_names = cars_meta['class_names']  # shape=(1, 196)
    class_names = np.transpose(class_names)
    print('class_names.shape: ' + str(class_names.shape))
    print('Sample class_name: [{}]'.format(class_names[8][0][0]))

    ensure_folder('data/train')
    ensure_folder('data/valid')
    ensure_folder('data/test')

    prepare_train_dataset(classes_path,training_annotations,training_images, desired_classes=[190,196,5,85])


    # shutil.rmtree('devkit')
        

