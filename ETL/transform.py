def transformer():
    print("I am in transformer function")
    from sklearn.metrics import confusion_matrix
    from keras.preprocessing.image import ImageDataGenerator
    from flask import jsonify
    from tensorflow import keras
    import os
    import boto3
    import botocore
    from ETL import config

    # print("I AM DOWNLOADING")
    # BUCKET_NAME = 'okayxray' # replace with your bucket name
    # KEY = 'model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5' # replace with your object key

    # s3 = boto3.resource(
    #                         's3',
    #                         aws_access_key_id = config.ACCESS_KEY,
    #                         aws_secret_access_key = config.SECRET_KEY
    #                     )

    # try:
    #     s3.Bucket(BUCKET_NAME).download_file(KEY, "tmp/ver3_model_softmax_3L64u_3Lnode_5epochs.h5")
    # except botocore.exceptions.ClientError as e:
    #     if e.response['Error']['Code'] == "404":
    #         print("The object does not exist.")
    #     else:
    #         print(e)

    # print("I AM DOWNLOADED")
    # print("get model")
    model = keras.models.load_model("model2.h5")
    # print("done")

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