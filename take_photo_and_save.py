import cv2
import face_recognition
import os



cam = cv2.VideoCapture(0)
img_counter = 0
path = '/Users/mohammadislam/Desktop/photo'
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        if cv2.contourArea(c)<30000:
            continue

        img_name = "opencv_frame_{}.png".format(img_counter)

        cv2.imwrite(os.path.join(path, img_name), frame1)
        cv2.waitKey(3000)

        img_counter+=1
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Take And Save Photo", frame2)




