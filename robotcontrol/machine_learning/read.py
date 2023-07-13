import cv2 as cv
import PIL as ts
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import matplotlib.pyplot as plt

#reads the image then returns it

# Grayscale, Gaussian blur, Otsu's threshold
image = cv.imread('Bild1.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), 0)
thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)
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

