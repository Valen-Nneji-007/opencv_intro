import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def grayHistrogram():
    Resize = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    #img = cv.resize(Resize,(342,512))
    img = cv.imread(Resize, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img,cmap='gray')

    hist = cv.calcHist([img],[0],None,[256],[0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel('# of Pixels')
    plt.show()

def colorHistrogram():
    Resize1 = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    img1 = cv.imread(Resize1)
    imgRGB = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)

    colors = ['b','g','r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB],[i],None,[256],[0,256])
        plt.plot(hist,colors[i])

    plt.xlabel('pixel intensity')
    plt.ylabel('# of Pixels')



    plt.show()



if __name__=='__main__':
    #grayHistrogram()
    colorHistrogram()