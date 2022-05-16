
# import cv2
# import face_recognition
from genericpath import exists
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

xpredictedPerson= ''

MODEL_LOCATION ='face_recognition_MMMM_V3'
model = load_model(MODEL_LOCATION) #load the model
print("loaded model from MODEL_LOCATION")

def generate_predictions_with_pre_trained_model(test_image_path, pre_model,predictedPerson):
    class_map = {0: 'akash', 1: 'arafat', 2: 'kabir', 3: 'shohag'}
    test_img = image.load_img(test_image_path, target_size=(128, 128))
    test_img_arr = image.img_to_array(test_img)/255.0
    test_img_input = test_img_arr.reshape((1, test_img_arr.shape[0], test_img_arr.shape[1], test_img_arr.shape[2]))

    global xpredictedPerson
    predicted_label = np.argmax(pre_model.predict(test_img_input))
    #print(predicted_label)
    predicted_person = class_map[predicted_label]
    predictedPerson = predicted_person
    xpredictedPerson=predictedPerson
    print(xpredictedPerson)
    plt.figure(figsize=(4, 4))
    plt.imshow(test_img_arr)
    plt.title("Predicted Label: {}".format(predicted_person))
    plt.grid()
    plt.axis('off')
    plt.show()
#generate_predictions_with_pre_trained_model('./kk.jpg', 'kabir', model)