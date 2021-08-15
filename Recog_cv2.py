import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('src/media/faces.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coord = trained_face_data.detectMultiScale(gray_img)

for (x, y, w, h) in face_coord:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# (x, y, w, h) = face_coord[5] # thisis to make a rectangle in individuel way, between the brackets can write from 0 to 11
# cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('Face Recognition App', img)
cv2.waitKey()

print('alles gut')
