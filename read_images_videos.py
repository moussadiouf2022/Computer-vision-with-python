import cv2 as cv
import numpy as np
import sys 
# ------------- Read image and video on open cv -----------------------------

im = cv.imread(r"C:\Users\hp\opencv_tuturial_python\image_3.jpg")
cv.imshow('Image_1',im)
cv.waitKey(0) 

capture = cv.VideoCapture(r"C:\Users\hp\Opencv_tuturial_python\Vid_1.mp4")

while True :
    isTrue,frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
