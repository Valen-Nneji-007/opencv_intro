import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def histEquai():
    Resize = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    #img = cv.resize(Resize,(342,512))
    img = cv.imread(Resize, cv.IMREAD_GRAYSCALE)
    hist = cv.calcHist([img],[0],None,[256],[0,256])
    cdf = hist.cumsum()
    cdfNorm = cdf * float(hist.max()) / cdf.max()


    plt.figure()
    plt.subplot(231)
    plt.imshow(img, cmap='gray')

    plt.subplot(234)
    plt.plot(hist)
    plt.plot(hist)
    plt.plot(cdfNorm, color='b')
    plt.xlabel('pixel intensity')
    plt.ylabel('# of pixels')



    equImg =cv.equalizeHist(img)
    equhist = cv.calcHist([img],[0],None,[256],[0,256])
    equcdf = equhist.cumsum()
    equcdfNorm =equcdf * float(equhist.max()) / equcdf.max()
    plt.subplot(232)
    plt.plot(equImg, cmap='gray')
    plt.subplot(235)
    plt.plot(equhist)
    plt.plot(equcdfNorm, color='b')
    plt.xlabel('pixel intensity')
    plt.ylabel('# of pixels')


    plt.show()


if __name__=='__main__':
    histEquai()