import cv2 as cv
import numpy as np

blank = np.zeros ((500,500,3),dtype = 'uint8')
# cv.imshow('Blank', blank)
# img = cv.imread('images/download.jpeg')
# cv.imshow('Download', img)
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green',blank)
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = -1)
# cv.imshow('Rectangle', blank)
# cv.circle(blank, (250,250), 40,(0,0,255), thickness = -1)
# cv.imshow("Circle" , blank)

cv.putText(blank, "Hello my name is Marvellous", (20,250),cv.FONT_ITALIC,1.0,(0,0,222,), 2)
cv.imshow('Text', blank)

cv.waitKey(0)