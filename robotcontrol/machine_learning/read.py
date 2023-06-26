import cv2 as cv

#reads the image then returns it
img = cv.imread('Photos/test.jpg')

#opens the image in a new window
cv.imshow('test', img)
#large images can go off screen

#reading videos

capture = cv.VideoCapture('Videos/test.mov')
#reading video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
#capture.release()
#cv.destroyAllWindows

#wait till cv.waitKey(3)