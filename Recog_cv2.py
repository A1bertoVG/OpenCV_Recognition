import cv2
from random import randrange

img = cv2.imread('src/media/faces.jpg')

cv2.imshow('Recognition', img)
cv2.waitKey()

print('alles gut')
