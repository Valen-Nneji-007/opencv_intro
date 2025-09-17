import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def rotation():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(Resize,(342,512))
    width,height,_ = img.shape
    T = cv.getRotationMatrix2D((width/2,height/2), 180, 1)
    imgTrans = cv.warpAffine(img,T,(width,height))
    cv.imshow('imgTrans', imgTrans)
    cv.waitKey(0)

if __name__=='__main__':
    rotation()