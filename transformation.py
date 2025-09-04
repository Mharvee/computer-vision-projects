import cv2 as cv
import numpy as np

img = cv.imread('images/download.jpeg')
cv.imshow('Download', img)
sphere = cv.imread('images/sphere.jpg')

def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100,-100)
cv.imshow('Translation', translated)

flip = cv.flip(img, 1, )
cv.imshow('Flipped', flip)

cv.waitKey(0)