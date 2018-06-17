import cv2
import numpy as np

from functions.toonify import *
from functions.rgb_greyscale import RGB2Greyscale

img = cv2.imread("kchorro.jpg")
cv2.imshow('kcchorro', img)
cv2.waitKey(0)

for i in range(2):
    img = cv2.pyrDown(img)
# img = cv2.pyrDown(img)
# cv2.imwrite('menor2.bmp', img)
# cv2.imshow('menor', img)
# cv2.waitKey(0)
for j in range(7):
    img = cv2.bilateralFilter(img, d=9, sigmaColor=9, sigmaSpace=7)
cv2.imwrite('bilateral.bmp', img)





img = cv2.pyrUp(img)
img = cv2.pyrUp(img)
cv2.imwrite('maior.bmp', img)
# cv2.imshow('menor', img)
# cv2.waitKey(0)

# # imgGrey = RGB2Greyscale(img)
# # cv2.imshow('kcchorro_cinza', imgGrey)
# # cv2.waitKey(0)
# gaussianImage = cv2.GaussianBlur(img, (7,7), 0)
# cv2.imwrite('1gaussianImage.bmp', gaussianImage)
# # cv2.imshow('gaussianImage', gaussianImage)
# # cv2.waitKey(0)
#
# medianImage = cv2.medianBlur(img, 7)
# cv2.imwrite('2medianImage.bmp', medianImage)
# # cv2.imshow('medianImage', medianImage)
# # cv2.waitKey(0)
#
# gMedianImage = cv2.medianBlur(gaussianImage, 7)
# cv2.imwrite('3gMedianImage.bmp', gMedianImage)
# # cv2.imshow('gMedianImage', gMedianImage)
# # cv2.waitKey(0)
#
# edges = cv2.Canny(gMedianImage, 75, 150, L2gradient=True)
# cv2.imwrite('edges.bmp', edges)
#
# se = cv2.getStructuringElement(1, (2,2))
# edges = cv2.dilate(edges, se)
# cv2.imwrite('edges2.bmp', edges)