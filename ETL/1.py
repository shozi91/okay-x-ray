from sklearn.metrics import confusion_matrix
from keras.preprocessing.image import ImageDataGenerator
from flask import jsonify
from tensorflow import keras
import os
import boto3
import botocore
import config

BUCKET_NAME = 'okayxray'
KEY = 'model/ver3_model_softmax_3L64u_3Lnode_5epochs.h5'

s3 = boto3.resource(
                        's3',
                        aws_access_key_id = config.ACCESS_KEY,
                        aws_secret_access_key = config.SECRET_KEY
                    )

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, "ver3_model_softmax_3L64u_3Lnode_5epochs.h5")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        print(e)