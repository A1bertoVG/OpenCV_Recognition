import cv2

video = cv2.VideoCapture('src/media/cars.mp4')

trained_car_data = cv2.CascadeClassifier('car.xml')

while True:
    succes_video, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    car_coord = trained_car_data.detectMultiScale(gray_frame)

    for (x, y, w, h) in car_coord:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Real Time Recognition', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

print('alles gut')
