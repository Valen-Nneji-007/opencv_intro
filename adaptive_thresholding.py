import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def adaptiveThresholding():
    Resize = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    #img = cv.resize(Resize,(342,512))
    imgGray = cv.imread(Resize, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.subplot(141)
    plt.imshow(imgGray,cmap='gray')
    plt.title('gray')
    

    plt.subplot(142)
    _, imgThres = cv.threshold(imgGray, 70,255, cv.THRESH_BINARY)
    plt.imshow(imgThres, cmap='gray')
    plt.title('global thres')

    plt.subplot(143)
    maxValue = 255
    blockSize = 7
    offsetC = 2
    imgMean = cv.adaptiveThreshold(imgGray,maxValue, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,blockSize, offsetC)
    plt.imshow(imgMean, cmap='gray')
    plt.title('mean thres')

    plt.subplot(144)
    maxValue = 255
    blockSize = 7
    offsetC = 2
    imgMean = cv.adaptiveThreshold(imgGray,maxValue, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,blockSize, offsetC)
    plt.imshow(imgMean, cmap='gray')
    plt.title('Gaussian thres')

    
    
    
    
    
    plt.show()





if __name__=='__main__':
    adaptiveThresholding()