import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def callback(input):
    pass

def averageFiltering():
    Resize = "C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg"
    #img = cv.resize(Resize,(342,512))
    img = cv.imread(Resize)

    winName = 'avg filter'
    cv.namedWindow(winName)
    cv.createTrackbar('n', winName,1,100,callback)

    height,width,_ = img.shape
    scale = 1/4
    width = int(width*scale)
    height = int(height*scale)
    img = cv.resize(img,(width,height))

    while True:
        if cv.waitKey(1)  == ord('q'):
            break

        n = cv.getTrackbarPos('n', winName)
        imgFIlter = cv.blur(img,(n,n))
        cv.imshow(winName, imgFIlter)



if __name__=='__main__':
    averageFiltering()