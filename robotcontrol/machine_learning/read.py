import cv2 as cv

#reads the image then returns it
img = cv.imread('Photos/test.jpg')

#reading videos

capture = cv.VideoCapture(0)

#Standard capture should be on port 0 or 1

cascade = open

#reading video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
#capture.release()
#cv.destroyAllWindows

#Contour Detection

#opens the image in a new window
cv.imshow('test', img)
#large images can go off screen
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('GRAY', gray)

canny = cv.canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_List, cv.CHAIN_APPROX_NONE)
# contours = python list of contours / contours which object is within which
# https://www.youtube.com/watch?v=oXlwWbU8l2o&t=777s