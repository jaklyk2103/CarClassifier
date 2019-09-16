# Run instruction
- download dataset to data/Dataset folder from:
 http://imagenet.stanford.edu/internal/car196/cars_train.tgz
- download devkit to data folder from:
https://ai.stanford.edu/~jkrause/cars/car_devkit.tgz
- run data_loader.py, desired classes param can be changed to choose other classes to preprocess
- run training.py, weights and model will be exported to h5 files, output file with classes names will be created

# Evaluation example
- insert test image to data/test folder
- run predict.py, changing path to saved weights and image name earlier
- predicted class name will be shown on screen