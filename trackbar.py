import cv2 as cv



def trackbarCallback():
    pass

def trackbar():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
    img = cv.resize(Resize,(342,512))

    windowName = 'trackbar demo'
    cv.namedWindow(windowName)
    cv.createTrackbar('B', windowName,0,255,trackbarCallback )
    cv.createTrackbar('G', windowName,0,255,trackbarCallback )
    cv.createTrackbar('R', windowName,0,255,trackbarCallback )

    while True:
        cv.imshow(windowName, img)

        if cv.waitKey(1) == ord('q'):
            break

        b = cv.getTrackbarPos('B', windowName)
        g = cv.getTrackbarPos('G', windowName)
        r = cv.getTrackbarPos('R', windowName)

        cv.circle(img,(300,200), 10, (b,g,r), -1)
        cv.circle(img, (250,215), 10, (b,g,r), -1)

    cv.destroyAllWindows()

if __name__=='__main__':
    trackbar()