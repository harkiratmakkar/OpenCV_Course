import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jpg")

gray_img = cv.cvtColor(img.copy(),cv.COLOR_BGR2GRAY)

gray_histogram = cv.calcHist([gray_img],[0], None, [256], [0, 255])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(gray_histogram)
plt.show()
cv.waitKey(0)
