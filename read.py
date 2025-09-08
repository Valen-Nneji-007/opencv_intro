import cv2 as cv  

resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

img = cv.resize(resize,(342,512))

# Reading videos
capture = cv.VideoCapture("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/video.mp4")

while True:
    isTrue, frame =capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows


#cv.imshow('image', img)
#cv.waitKey(0)


