def transformer():
    
    from sklearn.metrics import confusion_matrix
    from keras.preprocessing.image import ImageDataGenerator
    from flask import jsonify
    from tensorflow import keras
    from ETL import  config
    import os
    import boto3
    import botocore

    model_file = os.path.exists('./model2.h5')
    if model_file == True:
         model = keras.models.load_model("model2.h5")

    else:

        print("I AM DOWNLOADING")
        BUCKET_NAME = 'okayxray' # replace with your bucket name
        KEY = 'model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5' # replace with your object key
        s3 = boto3.resource(
            's3',
            aws_access_key_id = config.ACCESS_KEY ,
            aws_secret_access_key = config.SECRET_KEY
            )

        try:
            s3.Bucket(BUCKET_NAME).download_file(KEY, "model2.h5")
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                print(e)

        print("I AM DOWNLOADED")
        print("get model")
        
        model = keras.models.load_model("model2.h5")
        print("done")

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