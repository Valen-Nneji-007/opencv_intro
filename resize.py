import cv2 as cv
import matplotlib.pyplot as plt

def ImageResize():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(Resize,(342,512))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = img[286:300,311:400,:]
    height,width,_ = img.shape

    scale = 1/4

    interMethods = [
        cv.INTER_AREA,
        cv.INTER_LINEAR,
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ] 

    interpTitle = ['area','linear','nearest','cubic','lanczos4']

    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(img)

    for i in range(len(interMethods)):
        plt.subplot(2,3,i+2)
        imgResize = cv.resize(img,(int(width*scale),int(height*scale)),
        interpolation= interMethods[i])
        plt.imshow(imgResize)
        plt.title(interpTitle[i])
    plt.show()

if __name__=='__main__':
    ImageResize()