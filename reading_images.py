import cv2 as cv

img = cv.imread('images/download.jpeg')
cv.imshow('download', img)
cv.waitKey(0)

#Reading videos
capture = cv.VideoCapture('Videos/Fine girl.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xff == ord("q"):
        break
capture.release()
cv.destroyAllWindows()