import cv2 as cv 

img  = cv.imread('Photos/cat1.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cat2',gray)

img = cv.imread('Photos/NYC.jpg')
img = cv.resize(img,(1280,720))
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('NYC',blur)

canny = cv.Canny(img,125,175)
cv.imshow("canny",canny)
cv.waitKey(0)