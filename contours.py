import cv2 as cv


img = cv.imread('Photos/cat1.jpg')
#img = cv.resize(img,(720,360))
#cv.imshow("img",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("img",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow("blur",blur)

canny = cv.Canny(img,125,125)
#cv.imshow("canny",canny)


contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.waitKey(0)