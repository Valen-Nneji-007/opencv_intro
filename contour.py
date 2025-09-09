import cv2 as cv  
import numpy as np

resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

img = cv.resize(resize,(342,512))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} coutour(s) found')


cv.waitKey(0)