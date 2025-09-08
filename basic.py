import cv2 as cv
resize = cv.imread("C:/Users/Administrator/Documents/vs_code/computer_vision/opencv_intro/opencv_intro/opencv_intro/me.jpg")

img = cv.resize(resize,(342,512))

# # converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Blurring an image
# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(img, 100, 150)
cv.imshow('canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), 1)
cv.imshow('dilation',canny)

# Eroding
eroded = cv.erode(dilated,(3,3),1)
cv.imshow('eroded', eroded)

# cropped
crop = img[100:200, 50:300]
cv.imshow('crop', crop)

print(img.shape)
cv.waitKey(0)