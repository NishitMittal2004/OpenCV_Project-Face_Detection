import cv2

frameWidth = 640
frameHeight = 480
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
minArea = 500
color = (0,200,20)


cap = cv2.VideoCapture(1) # 0 for laptop webcam, 1 for other camera
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,500)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)


    for (x, y, w, h) in faces:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 200), 2)
            cv2.putText(img,"Face Detected",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break