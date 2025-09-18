import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def otsuThres():
    Resize = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    #img = cv.resize(Resize,(342,512))
    imgGray = cv.imread(Resize, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.subplot(131)
    plt.imshow(imgGray,cmap='gray')
    plt.title('gray')


    plt.subplot(132)
    thres = 70
    maxValue = 255
    _, imgThres = cv.threshold(imgGray,thres, maxValue,cv.THRESH_BINARY)
    plt.imshow(imgThres, cmap='gray')
    plt.title('global')

    plt.subplot(133)
    thres = 70
    maxValue = 255
    _, imgOtsu = cv.threshold(imgGray,thres, maxValue,cv.THRESH_BINARY+cv.THRESH_OTSU)
    plt.imshow(imgOtsu, cmap='gray')
    plt.title('otsu')

    hist = cv.calcHist([imgGray],[0],None,[256],[0,256])
    plt.figure()
    plt.plot(hist)
    plt.xlabel('intensity')
    plt.ylabel('# of pixels')

    plt.show()

if __name__=='__main__':
    otsuThres()