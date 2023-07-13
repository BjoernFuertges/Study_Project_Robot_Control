import cv2 as cv
import PIL as ts
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import matplotlib.pyplot as plt

#reads the image then returns it

myconfig = r"--psm 11 --oem3"

# Grayscale, Gaussian blur, Otsu's threshold
image = cv.imread('C:\Users\jumla\OneDrive\Desktop\Studienprojekt\Studienprojekt1_Robotersteuerung\robotcontrol\machine_learning\Photos\Bild1.png')
print(image)

text = pytesseract.image_to_string(ts.Image.open(image), config=myconfig)
print(text)

#capture = cv.VideoCapture(0)

#Standard capture should be on port 0 or 1

#cascade = open

#reading video frame by frame
#while True:
#    isTrue, frame = capture.read()
#    cv.imshow('Video', frame)

    #if cv.waitKey(20) & 0xFF==ord('d'):
     #   break
#capture.release()
#cv.destroyAllWindows

#Contour Detection

#opens the image in a new window
#cv.imshow('test', img)
#large images can go off screen
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('GRAY', gray)

#canny = cv.canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)
#
#contours, hierarchies = cv.findContours(canny, cv.RETR_List, cv.CHAIN_APPROX_NONE)
# contours = python list of contours / contours which object is within which
# https://www.youtube.com/watch?v=oXlwWbU8l2o&t=777s

