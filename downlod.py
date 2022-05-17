from boto3.session import Session

from recognition import generate_predictions_with_pre_trained_model

import os

import numpy as np
import boto3
from boto3.session import Session
import tensorflow as tf
if tf.executing_eagerly():
    tf.compat.v1.disable_eager_execution()
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import matplotlib.pyplot as plt

MODEL_LOCATION = 'face_recognition_MMMM_V3'
model = load_model(MODEL_LOCATION)  # load the model
print("loaded model from MODEL_LOCATION")


access_key = 'AKIASYJI4PBHNJY72AVK'
secret_access_key = '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'

client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)


session = Session(aws_access_key_id=access_key,
                  aws_secret_access_key=secret_access_key)


def download():
    path = '/Users/mohammadislam/Desktop/photo'
    access_key = 'AKIASYJI4PBHNJY72AVK'
    secret_access_key = '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'

    session = Session(aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)

    s3 = session.resource('s3')
    bucket = 'employbucket'
    my_bucket = s3.Bucket(bucket)
    for s3_files in my_bucket.objects.all():
        p = s3_files.key
        my_bucket.download_file(p, path + '/' + p)

    for file in os.listdir():
        if '.jpg' in file:
            upload_file_bucket = 'employbucket'
            upload_file_key = str(file)
           # generate_predictions_with_pre_trained_model(upload_file_key, 'kabir', model)
            os.remove(file)


while True:
    bucket = 'employbucket'
    s3 = session.resource('s3')
    my_bucket = s3.Bucket(bucket)
    if my_bucket is not None:
        download()
