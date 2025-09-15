import cv2 as cv

def callback():
    pass

def imageBlending():
    resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

    img = cv.resize(resize,(342,512))

    height, width, _ = img.shape
    
    img2 = cv.imread('C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/woman.jpg')
    
    x0 = 300
    y0 = 0

    img2 = img2[y0:y0+height, x0:x0+width]

    windowName = 'image blending'
    cv.namedWindow(windowName)

    scale = 100
    cv.createTrackbar('alpha',windowName, 0,1*scale,callback)
    cv.createTrackbar('gamma',windowName,0,255,callback)

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        alpha  = cv.getTrackbarPos('alpha', windowName)/scale
        beta = 1-alpha
        gamma = cv.getTrackbarPos('gamma',windowName)

        imgBlend = cv.addWeighted(img,alpha, img2, beta, gamma)

        cv.imshow(windowName,imgBlend)

    cv.destroyAllWindows()

if __name__=='__main__':
    imageBlending()



