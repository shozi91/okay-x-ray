def transformer():
    
    from sklearn.metrics import confusion_matrix
    from keras.preprocessing.image import ImageDataGenerator
    from flask import jsonify
    from tensorflow import keras
    import os
    import boto3
    

    s3 = boto3.client('s3') #low-level functional API
    #locale machine line
    s3.download_file(Bucket='okayxray',Key='model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5',Filename= "model.h5")
    model = keras.models.load_model("model.h5")

    #heroku code line
    #s3.download_file(Bucket='okayxray',Key='model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5',Filename= "/tmp/model.h5")
    #model = keras.models.load_model("/tmp/model.h5")


    #read test images in model
    test_gen = ImageDataGenerator(rescale = 1./255)
    test_set = test_gen.flow_from_directory(os.path.join('Upload'),
                                        target_size = (500,
                                                       500),
                                        batch_size = 1,
                                        class_mode = None,
                                        color_mode = 'grayscale',
                                        shuffle=False)

    #probability (normal/sick)
    predictions = model.predict(test_set)
    


    return predictions

if __name__ == '__main__':
    transformer()