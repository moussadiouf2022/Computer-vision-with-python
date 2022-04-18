import cv2 as cv
import numpy as np


# simulation choice
Paint_image = 0;
Draw_rectangle = 0;
Draw_circle = 0;
Draw_line = 0;
Write_text = 0;


blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)

#1 - Paint the image a certain colour
if Paint_image == 1:
    blank [200:300,300:400] = 0,0,255
    cv.imshow('Green',blank)


# 2 - Draw a rectangle 
if Draw_rectangle == 1:
    cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
    cv.imshow('Rectangle',blank)


# 3 - Draw A Circle
if Draw_circle == 1:
    cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255),thickness=-1)
    cv.imshow('Circle',blank)


# 4 - Draw a line 
if Draw_line == 1:
    cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),thickness=3)
    cv.imshow('Line',blank)


# 5 - Write text
if Write_text == 1:
    cv.putText(blank,'Hello My name is Moussa',(0,255), cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0),2)
    cv.imshow('Text',blank)


cv.waitKey(0)