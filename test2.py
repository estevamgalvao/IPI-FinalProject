import cv2
import copy
import numpy as np

adressOriginalImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/originalImages/'


image = cv2.imread(adressOriginalImages + 'vaca3.jpg')
imageAux = copy.copy(image)

numDownsamples = 2
numBilateralFiltering = 14

imageBlured = cv2.medianBlur(imageAux, 7)
cv2.imwrite('imageBlured.bmp', imageBlured)

imageAux = imageBlured

imageEdges = cv2.Canny(imageAux, 75, 125, L2gradient=True)
imageEdges = cv2.bitwise_not(imageEdges)
print(imageEdges.shape)
cv2.imwrite('imageEdges.bmp', imageEdges)

imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB)

print(imageEdges.shape)
cv2.imwrite('imageEdges22.bmp', imageEdges)
imageAux = cv2.bilateralFilter(imageAux, 5, 150, 150)

# sElement = cv2.getStructuringElement(1, (2,2))
# imageEdgesDilated = cv2.dilate(imageEdges, sElement)
# imageEdgesDilated = cv2.cvtColor(imageEdgesDilated, cv2.COLOR_GRAY2RGB)

# for _ in range(numDownsamples):
#     imageAux = cv2.pyrDown(imageAux)
#
# for _ in range(numBilateralFiltering):
#     imageAux = cv2.bilateralFilter(imageAux, 5, 15, 15)
#
# for _ in range(numDownsamples):
#     imageAux = cv2.pyrUp(imageAux)

imageFiltered = imageAux
cv2.imwrite('imageFiltered.bmp', imageFiltered)
# imageBlured = cv2.medianBlur(imageAux, 7)

imageKmeans = imageFiltered.reshape((-1, 3))
imageKmeans = np.float32(imageKmeans)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
k = 24

_ret, _label, _center = cv2.kmeans(imageKmeans, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

_center = np.uint8(_center)
_res = _center[_label.flatten()]
_res2 = _res.reshape(image.shape)
cv2.imwrite('res2.bmp', _res2)

        # final _image
imageCartoon = cv2.bitwise_and(_res2, imageEdges)





# imageCartoon = cv2.bitwise_and(imageEdgesDilated, imageAux)
cv2.imwrite('imageCartoon.bmp', imageCartoon)