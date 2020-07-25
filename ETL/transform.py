def transformer():
        
    import pandas as pd
    import numpy as np
    #from PIL import Image

    from sklearn.metrics import confusion_matrix
    
    from keras.preprocessing.image import ImageDataGenerator, array_to_img

    from tensorflow import keras

    from datetime import datetime
    import os

    root_path = os.path.dirname(os.getcwd())
    model = keras.models.load_model(os.path.join(f'{root_path}\\..\\New folder\\ver2_model_softmax_3L64u_3Lnode_10epochs.h5')) 

    hyper_dimension = 500
    hyper_mode = 'grayscale'

    test_gen = ImageDataGenerator(rescale = 1./255)

    test_set = test_gen.flow_from_directory(f'{root_path}\\Upload\\Saved',
                                        target_size = (hyper_dimension,
                                                       hyper_dimension),
                                        batch_size = 1,
                                        class_mode = 'categorical',
                                        color_mode = hyper_mode,
                                        shuffle=False)

    predictions = model.predict(test_set)
    y_classes = predictions.argmax(axis=-1)

    return (predictions, y_classes)

if __name__ == '__main__':
    transformer()