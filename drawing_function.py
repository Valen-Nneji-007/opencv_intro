import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def drawingFunctions():
    resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

    img = cv.resize(resize,(342,512))
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    white =(255, 255, 255)
    cv.line(img,(30,400),(296,96),white,4)

    r,c,d =img.shape
    offset = 10
    cv.rectangle(img,(offset,offset),(c-offset,r-offset),white,4)


    cv.circle(img,(187,147), 10, white, -1 )

    cv.ellipse

    cv.ellipse(img,)

    cv.imshow('drawing', img)
    cv.waitKey(0)

    


if __name__ == '__main__':
    drawingFunctions()