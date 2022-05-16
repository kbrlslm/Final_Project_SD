
import cv2
import face_recognition
import os
import numpy as np
import boto3
import os, glob

from boto3.session import Session
def delete_file():
    bucket = 'employbucket'
    access_key = 'AKIASYJI4PBHNJY72AVK'
    secret_access_key = '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'

    client = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key)

    def del_file(filename):
        client.delete_object(Bucket = bucket, Key = filename)

    all_objects = client.list_objects(Bucket=bucket)
    if 'Contents' in all_objects:
        for a in all_objects['Contents']:
            del_file(a['Key'])

while True:
    delete_file()





