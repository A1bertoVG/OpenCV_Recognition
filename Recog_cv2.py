import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontaface_defailt.xml')

img = cv2.imread('src/media/faces.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''face_coord = trained_face_data.detectMultiScale(gray_img)

print(face_coord)'''

cv2.imshow('Recognition', gray_img)
cv2.waitKey()

print('alles gut')
