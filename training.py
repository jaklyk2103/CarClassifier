import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from model import get_full_model, get_mobile_model
import tensorflow as tf
import json

img_width, img_height = 224, 224
num_channels = 3
train_data = 'data/train'
valid_data = 'data/valid'
num_classes = 2
num_train_samples = 196
num_valid_samples = 70
verbose = 1
batch_size = 16
num_epochs = 10
patience = 50
learning_rate = 0.0001

if __name__ == '__main__':
    
    model = get_full_model(learning_rate)
    

    #data augmentation configuration
    train_data_gen = ImageDataGenerator(rotation_range=20.,
                                        width_shift_range=0.1,
                                        height_shift_range=0.1,
                                        zoom_range=0.2,
                                        horizontal_flip=True)
    valid_data_gen = ImageDataGenerator()
   
    early_stopping = EarlyStopping('val_acc', patience=patience)
    learning_rate_reducer = ReduceLROnPlateau('val_acc', factor=0.1, patience=int(patience / 4), verbose=1)
    callbacks = [ early_stopping, learning_rate_reducer]
   

    # generators
    train_generator = train_data_gen.flow_from_directory(train_data, (img_width, img_height), batch_size=batch_size,shuffle=True,
                                                         class_mode='categorical')
    valid_generator = valid_data_gen.flow_from_directory(valid_data, (img_width, img_height), batch_size=batch_size,shuffle=True)
    
    hist = model.fit_generator(
        train_generator,
        steps_per_epoch=num_train_samples / batch_size,
        validation_data=valid_generator,
        validation_steps=num_valid_samples / batch_size,
        epochs=num_epochs,
        verbose=verbose,
        callbacks=callbacks)

    keras_file = "transfer.h5"
    keras.models.save_model(model,keras_file)
    model.save_weights("transfer_weights.h5")
    with open('file.json', 'w') as f:
        json.dump(str(hist.history), f)


