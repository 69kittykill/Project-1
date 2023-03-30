import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#lower threshold for red
    lower_red = np.array([160,50,50])
    upper_red = np.array([180,255,255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
    mask = mask_green + mask_red
    res = cv2.bitwise_and(frame, frame, mask = mask)
    # res2 = cv2.bitwise_and(frame, frame, mask_green = mask_green)
    
    # print(frame)
    # print(mask)
    # print(res)
# Display the resulting frame
    cv2.imshow('Frame', frame)
    # cv2.imshow('Mask', mask)
    cv2.imshow('Results', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows(0)