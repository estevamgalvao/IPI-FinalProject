import datetime
import cv2
import numpy as np

from functions.cannythreshold import *

adressOriginalImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/originalImages/'
adressBluredImages    = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bluredImages/'
adressEdgesImages     = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/edgesImages/'
adressbFilteredImages = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bFilteredImages/'
adressRes2Images      = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/quantizedImages/'
adressCartoonImages   = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/cartoonImages/'


typeImage = '.jpg'
i = 43
# imageAux = originalImagesArray[i]
# imageAux = cv2.imread(adressOriginalImages + '0' + str((i + 1)) + '.jpg')
imageAux = cv2.imread(adressOriginalImages + '071.jpg')

# imageAux = cv2.imread('img9.jpg')
print(adressOriginalImages + 'img' + str((i + 1)) + '.jpg')
# cv2.imshow('original', imageAux)
# cv2.waitKey(0)
# imageAux = cv2.imread(adressOriginalImages + 'img8.jpg')
# imageAux = copy.copy(image)
a = datetime.datetime.now()

# h, w = imageAux.shape[:2]


imageBlured = cv2.medianBlur(imageAux, 5)
cv2.imwrite('imageBlured' + str((i+1)) + typeImage, imageBlured)
# cv2.imwrite(adressBluredImages + 'SEMGLOBimageBlured' + str((i+1)) + typeImage, imageBlured)

lowThreshold, highThreshold = cannyThreshold(imageBlured)
print(lowThreshold)
print(highThreshold)
imageEdges = cv2.Canny(imageBlured, lowThreshold, highThreshold, L2gradient=True)
imageEdges = cv2.bitwise_not(imageEdges) # inverto as linhas de branco para preto e o fundo de preto para branco
cv2.imwrite('imageEdges' + str((i+1)) + typeImage, imageEdges)
# cv2.imwrite(adressEdgesImages + 'SEMGLOBimageEdges' + str((i+1)) + typeImage, imageEdges)


imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB) # faço a img ter 3 canais novamente

imageFiltered = cv2.bilateralFilter(imageBlured, 5, 35, 35)
cv2.imwrite('imageFiltered' + str((i+1)) + typeImage, imageFiltered)
# cv2.imwrite(adressbFilteredImages + 'SEMGLOBimageFiltered' + str((i+1)) + typeImage, imageFiltered)


imageKmeans = imageFiltered.reshape((-1, 3))
imageKmeans = np.float32(imageKmeans)
quantizationCriteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 1)
kClusters = 24

_ret, _label, _center = cv2.kmeans(imageKmeans, kClusters, None, quantizationCriteria, 5, cv2.KMEANS_RANDOM_CENTERS)

_center = np.uint8(_center)
_res = _center[_label.flatten()]
imageQuantized = _res.reshape(imageAux.shape)
cv2.imwrite('imageQuantized' + str((i+1)) + typeImage, imageQuantized)
# cv2.imwrite(adressRes2Images + 'SEMGLOBimageQuantized' + str((i+1)) + typeImage, imageQuantized)


imageCartoon = cv2.bitwise_and(imageQuantized, imageEdges)
cv2.imwrite('imageCartoon' + str((i+1)) + typeImage, imageCartoon)
# cv2.imwrite(adressCartoonImages + 'SEMGLOBimageCartoon' + str((i+1)) + typeImage, imageCartoon)
# cv2.imshow('cartoon', imageCartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
b = datetime.datetime.now()
print("\nThe program took %d hours, %d minutes and %d seconds to execute"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))
