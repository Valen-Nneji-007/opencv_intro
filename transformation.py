import cv2 as cv  
import numpy as np

resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

img = cv.resize(resize,(342,512))

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
#  x --> Right 
#  y --> Down

translated =translate(img, 100, 100)
cv.imshow('Translate', translated)

# Rotate
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotate', rotated)

# flip
flip =cv.flip(img, 0)
cv.imshow('flip', flip)


# crop
crop = img[100:200, 200:300]
cv.imshow('crop', crop)

cv.waitKey(0)