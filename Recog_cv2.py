import cv2
from random import randrange

img = cv2.imread('src/media/car_img.jpg')

trained_car_data = cv2.CascadeClassifier('car.xml')  # https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_coord = trained_car_data.detectMultiScale(gray_img)

# print(car_coord)

for (x, y, w, h) in car_coord:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Car recognition', img)
key = cv2.waitKey()
if key == 81 or key == 113:
    cv2.destroyAllWindows()

print('alles gut')
