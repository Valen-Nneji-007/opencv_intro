import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvColorSegmentation():
    resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(resize,(342,512))
    imgRBG = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    debug = 1

    if __name__ =='__main__':
        hsvColorSegmentation()

