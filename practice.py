import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def practice():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(Resize,(342,512))

    diff = [cv.cvtColor(img,cv.COLOR_BGR2GRAY),
            cv.cvtColor(img,cv.COLOR_BGR2RGB),
            cv.cvtColor(img,cv.COLOR_BGR2HSV),
            cv.cvtColor(img,cv.COLOR_BGR2HLS),
            cv.cvtColor(img,cv.COLOR_BGR2LAB),
            cv.cvtColor(img,cv.COLOR_BGR2LUV)]
    
    diffNames = ['Gray', 'Rgb', 'Hsv', 'Hls', 'Lab', 'Luv']
    
    for i in range(len(diff)):
        #plt.figure()
        plt.subplot(3,2,1+i)
        plt.imshow(diff[i])
        plt.title(diffNames[i])

    plt.show()

if __name__=='__main__':
    practice()
        
