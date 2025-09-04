import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading videos
capture = cv.VideoCapture('Videos/Fine girl.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:  # if no frame is returned (end of video or error)
        break

    resized_frame = rescaleFrame(frame)

    # cv.imshow('Video', frame)   # show original if you want
    cv.imshow('Video Resized', resized_frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
