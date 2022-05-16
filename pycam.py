import cv2
import face_recognition
import os
import numpy as np
import boto3
import time
from picamera.array import PiRGBArray



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
    ret, frame = cam.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        kk = cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
        face_image = kk[top:bottom, left:right]
        cv2.imshow("Take And Save Photo", face_image)

        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, face_image)
        img_counter+=1

        for file in os.listdir():
            if '.png' in file:
                upload_file_bucket = 'employbucket'
                upload_file_key = 'photo/' + str(file)
                client.upload_file(file, upload_file_bucket, upload_file_key)
                os.remove(file)


    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()