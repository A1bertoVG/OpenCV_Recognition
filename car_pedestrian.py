import cv2

trained_car_data = cv2.CascadeClassifier('car.xml')
trained_fullbody_data = cv2.CascadeClassifier('haarcascade_fullbody.xml')

video = cv2.VideoCapture('src/media/car-ped.mp4')
# video = cv2.VideoCapture('src/media/car-ped2.mp4')


while True:
    succes_video, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    car_coord = trained_car_data.detectMultiScale(gray_frame)
    pedestrian_coord = trained_fullbody_data.detectMultiScale(gray_frame)

    for (x, y, w, h) in car_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in pedestrian_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Auto / Pedestrian recognition', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

print('alles gut')
