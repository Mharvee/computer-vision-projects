import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/download.jpeg')
cv.imshow('Download', img)
sphere = cv.imread('images/sphere.jpg')
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
#
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

plt.imshow(img)
plt.show()




cv.waitKey(0)