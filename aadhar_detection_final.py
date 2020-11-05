import cv2
import re
import pytesseract
from pytesseract import Output
img = cv2.imread(#specify the name of the image here)
#regular expresiion representing a 4 digit number
aadhar_pattern = ("^SW[0-9]{4}$")
#now we are extracting the data from the image and storing it in a dictionry
d = pytesseract.image_to_data(img, output_type=Output.DICT)
#the first two consecutive 4 digit numbers will be the first2 segments of the adhar card hence loop runs only twice
for i in range(2):
    if (int(d['conf'][i]) > 60 and re.match(aadhar_pattern, d['text'][i])): #matching the RE with aadhar number
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,255), 10) # drawing a very thick rectangle that masks the first 2 aadhar segmenst

cv2.imshow('img', img)
cv2.waitKey(0)