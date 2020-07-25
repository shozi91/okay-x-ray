def transformer():
    print("I am in transformer function")
    from sklearn.metrics import confusion_matrix
    from keras.preprocessing.image import ImageDataGenerator
    from flask import jsonify
    from tensorflow import keras
    import os
    import boto3

    s3 = boto3.client('s3') #low-level functional API
    s3.download_file(Bucket='okayxray',Key='model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5',Filename= "/tmp/ver3_model_softmax_3L64u_3Lnode_5epochs.h5")
    #model = keras.models.load_model("C:\\Users\\Matth\\Documents\\GitHub\\model_2\\model2.h5")
    model = keras.models.load_model("/tmp/ver3_model_softmax_3L64u_3Lnode_5epochs.h5")

    hyper_dimension = 500
    hyper_mode = 'grayscale'

    test_gen = ImageDataGenerator(rescale = 1./255)
    #s3.download_file(Bucket='okayxray',Key=f'upload/{file_name}',Filename= f"/tmp/{file_name}")
    # we have to add the right path for uploaded pic to read
    test_set = test_gen.flow_from_directory(os.path.join('Upload'),
                                        target_size = (hyper_dimension,
                                                       hyper_dimension),
                                        batch_size = 1,
                                        class_mode = None,
                                        color_mode = hyper_mode,
                                        shuffle=False)

    #probability (normal/sick)
    predictions = model.predict(test_set)

    return predictions

if __name__ == '__main__':
    transformer()