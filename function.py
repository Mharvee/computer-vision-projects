import cv2 as cv


img = cv.imread('images/download.jpeg')
cv.imshow('Download', img)
sphere = cv.imread('images/sphere.jpg')

#Greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (15,15), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


resized = cv.resize(sphere, (500,500))
cv.imshow('resized', resized)

cv.waitKey(0)