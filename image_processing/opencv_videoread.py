import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True:
    
    _, frame = cap.read()

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_centre = frame[cx, cy]
    print(pixel_centre)

    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), 2)



    cv2.imshow("Frame", hsvImg)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
