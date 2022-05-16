import cv2
import face_recognition
import os
import boto3
from boto3.session import Session
from recognition import generate_predictions_with_pre_trained_model
import tensorflow as tf
if tf.executing_eagerly():
   tf.compat.v1.disable_eager_execution()
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from gmail import send_email


MODEL_LOCATION ='face_recognition_MMMM_V3'
model = load_model(MODEL_LOCATION) #load the model
print("loaded model from MODEL_LOCATION")

access_key = 'AKIASYJI4PBHNJY72AVK'
secret_access_key = '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'

session = Session(aws_access_key_id=access_key,
                  aws_secret_access_key=secret_access_key)

client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)
bucket = 'employbucket'
all_objects = client.list_objects(Bucket = bucket)
s3 = session.resource('s3')
my_bucket = s3.Bucket(bucket)

path = '/Users/mohammadislam/Desktop/photo'

def send_file():
    cam = cv2.VideoCapture(0)
    cam.set(3, 1920)
    cam.set(4, 1080)
    img_counter = 0
    while cam.isOpened():
        ret, ll = cam.read()
        rgb_frame = ll[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            kk = cv2.rectangle(ll, (left, top), (right, bottom), (0, 0, 255), 2)
            face_image = kk[top:bottom, left:right]
            cv2.imshow("Take And Save Photo", face_image)
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, face_image)
            img_counter += 1

            for file in os.listdir():
                if '.png' in file:
                    upload_file_bucket = 'employbucket'
                    upload_file_key = str(file)
                    client.upload_file(file, upload_file_bucket, upload_file_key)
                    os.remove(file)

        if cv2.waitKey(10) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()





x=''
def run_file():
    path = '/Users/mohammadislam/Desktop/photo'
    s3=session.resource('s3')
    bucket = 'employbucket'
    my_bucket = s3.Bucket(bucket)
    if my_bucket is not None:
        for s3_files in my_bucket.objects.all():
            p = s3_files.key
            my_bucket.download_file(p, p)

    for file in os.listdir():
        if '.jpg' in file:
            upload_file_bucket = 'employbucket'
            upload_file_key = str(file)
            global x
            generate_predictions_with_pre_trained_model(upload_file_key, model, predictedPerson=x)
            send_email(x, file)
            os.remove(file)



def delete_file():
    client = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key)

    def del_file(filename):
        client.delete_object(Bucket=bucket, Key=filename)

    all_objects = client.list_objects(Bucket=bucket)
    if 'Contents' in all_objects:
        for a in all_objects['Contents']:
            del_file(a['Key'])




while True:
    if my_bucket is not None:
        run_file()
    delete_file()






