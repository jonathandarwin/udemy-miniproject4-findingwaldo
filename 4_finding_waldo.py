import cv2
import numpy as np

# cari gambar yang ingin dicari dari scene gambar yang disediakan
# dengan menggunakan matchTemplate
# caranya dengan cek satu2 dari sudut atas scene gambar smpai sudut bawah scene gambar
image = cv2.imread('WaldoBeach.jpg')
cv2.imshow('Where is waldo?', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('waldo.jpg', 0)

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

# creating bounding box
topLeft = maxLoc
bottomRight = (topLeft[0] + 50, topLeft[1] + 50)
cv2.rectangle(image, topLeft, bottomRight, (0, 0, 255), 5)

cv2.imshow('Where is waldo?', image)
cv2.waitKey(0)