import cv2
import face_recognition
import os
import numpy as np
import boto3
import time
from datetime import datetime



def send_file():
    access_key = 'AKIASYJI4PBHNJY72AVK'
    secret_access_key = '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'

    client = boto3.client('s3',
                          aws_access_key_id = access_key,
                          aws_secret_access_key = secret_access_key)

    cam = cv2.VideoCapture(0)
    cam.set(3,1920)
    cam.set(4,1080)
    img_counter = 0
    #path = '/Users/mohammadislam/Desktop/photo'
    while cam.isOpened():
        ret, ll = cam.read()
        rgb_frame = ll[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            kk = cv2.rectangle(ll, (left, top), (right, bottom), (0,0,255), 2)
            face_image = kk[top:bottom, left:right]
            cv2.imshow("Take And Save Photo", face_image)
            now = datetime.now()
            dt_string = now.strftime("%m_%d_%Y_%H:%M:%S")
            img_name = dt_string + '.jpg'
            print(img_name)
            cv2.imwrite(img_name, face_image)


            for file in os.listdir():
                if '.jpg' in file:
                    upload_file_bucket = 'employbucket'
                    upload_file_key =  str(file)
                    client.upload_file(file, upload_file_bucket, upload_file_key)
                    os.remove(file)


        if cv2.waitKey(10) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

send_file()