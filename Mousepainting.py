import cv2 as cv
import os


def drawCircle(event, x,y, flags, param):
    img = param
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),10,(0,0,255), -1)


def doubleClicking():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

    img = cv.resize(Resize,(342,512))

    windowName = 'drawing app'
    cv.namedWindow(windowName)
    cv.setMouseCallback(windowName, drawCircle, img)

    while True:
        cv.imshow(windowName, img)
        if cv.waitKey(1) == ord('q'):
            break

class DrawingApp:
    def __init__(self,imagePath):
        self.imagePath = imagePath
        self.startX, self.startY = 0,0
        self.isDrawing = False

    def drawLine(self, event,x,y,flags, param):
        img = param
        if event == cv.EVENT_LBUTTONDOWN:
            self.isDrawing = True
            self.startX, self.startY = x, y
        elif event == cv.EVENT_MOUSEMOVE and self.isDrawing:
            cv.line(img,(self.startX, self.startY), (x,y), (255,255,255), 3)
        elif event == cv.EVENT_LBUTTONUP:
            self.isDrawing = False
            cv.line(img,(self.startX, self.startY), (x,y), (255,255,255), 3)

    def run(self):
        Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")
        img = cv.resize(Resize,(342,512))

        windowName = 'drawing app'
        cv.namedWindow(windowName)
        cv.setMouseCallback(windowName,self.drawLine, img)

        while True:
            cv.imshow(windowName, img)
            if cv.waitKey(1) == ord('q'):
                break





        

def holdAndDragDrawing():
    Resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

    img = cv.resize(Resize,(342,512))
    app = DrawingApp(img)
    app.run()



    




if __name__=='__main__':
    #doubleClicking()
    holdAndDragDrawing()
