import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

# 1. paint the image a certain color
#blank[:]= 0,0,255

rect = cv.rectangle(blank,(250,200),(300,500),(0,0,255), 5)
#rect = cv.rectangle(blank,(blank.shape[1]//2),(blank.shape[0]//2), (0,255,0), 3)
#cv.imshow('Blank', rect)

#img = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
#cv.imshow('image', img)

# draw  a circle
#circle = cv.circle(blank,(250,250),100,(0,255,0),3)
#cv.imshow('circle',circle)

# Draw a line
# line= cv.line(blank,(300,250),(400,450),(255,255,255),3)
# cv.imshow('line',line)

# Draw a text on an image
text = cv.putText(blank, 'Valentine is great', (10,20), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,255),3)
cv.imshow('text',text)
cv.waitKey(0)
