import cv2 as cv
import PIL as pil
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jumla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts'
import matplotlib.pyplot as plt

#reads the image then returns it

myconfig = r"--psm 11"

imagepath = "C:/Users/jumla/Desktop/Studienprojekt/Studienprojekt1_Robotersteuerung/robotcontrol/machine_learning/Photos/robot_picture_aoi.jpg"
image = cv.imread(imagepath)
print(image)
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imwrite("gray_image.png", gray_image)
thresh = cv.threshold(gray_image, 130, 255, cv.THRESH_BINARY)[1]
cv.imwrite("treshhold.png", thresh)
denoised = cv.fastNlMeansDenoisingColored(image)
cv.imwrite("denoised.png", denoised)
# Create custom kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))

# Perform closing (dilation followed by erosion)
close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
cv.imwrite("morph.png", close)

# Invert image to use for Tesseract
result = 255 - close
cv.imshow('gray', gray_image)
cv.imshow('thresh', thresh)
cv.imshow('close', close)
cv.imwrite("close.png", close)
cv.imshow('result', result)
cv.imwrite("result.png", result)
cv.imshow('denoised', denoised)

# Throw image into tesseract
#print(pytesseract.image_to_string(result))
cv.waitKey()


#text = pytesseract.image_to_string(pil.Image.open(imagepath), config=myconfig)


#print(text)

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

