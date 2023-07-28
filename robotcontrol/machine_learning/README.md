# Installation

sudo needed
``` bash
pip install opencv-contrib-python
pip install caer
pip install pytesseract
pip install numpy
pip install matplotlib
pip install opencv-python
pip install pillow
```

tesseract installer needed: 
https://github.com/UB-Mannheim/Tesseract_Dokumentation/blob/main/Tesseract_Doku_Windows.md

add tesseract to path
normal install path is: 
"C:\Program Files\Tesseract-OCR"

to run pytesseract needs to know location of the script via a code snippet at the top
"pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'"

More information on machine learning: 
https://docs.opencv.org/3.4/dc/dd6/ml_intro.html

# Ideen und weitere Arbeitsschritte

Grayscaling und Contourfilter could get better results for textdetection

1.) Test robot camera and try to read this image

if (image good enough to output room number)
    further development
    training a OCR modell optical character recognition
    
else
    cry?
    indoormapping through left hand rule?
    orientation through other methods?
    

