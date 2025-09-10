import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvColorSegmentation():
    #root = os.getcwd()
    #imgPath = os.path.join("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    #imgPath = os.path.join(root, 'demoImages\\cutepic1.jpg')
    #img = cv.imread(imgPath)
    resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(resize,(342,512))
    imgRBG = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerBound = np.array([0,0,50])
    upperBound = np.array([50,120,100])
    mask = cv.inRange(hsv,lowerBound,upperBound)

    cv.imshow('jiggy', mask)
    cv.waitKey(0)

    plt.figure()
    plt.imshow(imgRBG)
    plt.show()

    debug = 1

if __name__ =='__main__':
    hsvColorSegmentation()

