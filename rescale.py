import cv2 as cv 

img = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
#cv.imshow('me', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img, scale=0.1)
cv.imshow('img', resized_img)

capture = cv.VideoCapture("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/video.mp4")

while True:
    isTrue, frame =capture.read()
    
    frame_resized =rescaleFrame(frame,scale=0.2)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

cv.waitKey(0)
