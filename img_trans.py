import cv2 as cv
import numpy as np

img = cv.imread('Photos/NYC.jpg')

img = cv.resize(img,(640,360))

def translate(img,x,y):#to shift the img
    trans = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,trans,dimensions)
    

img1 = translate(img,100,100)
img2 = translate(img,-100,100)
img3 = translate(img,100,-100)
img4 = translate(img,-100,-100)

#cv.imshow("img1",img1)
#cv.imshow("img2",img2)
#cv.imshow("img3",img3)
#cv.imshow("img4",img4)


def rotate(img , angle,rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,189)
cv.imshow("rotated",rotated)

cv.waitKey(0)