import cv2
import copy
import numpy as np

adressOriginalImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/originalImages/'

i = 0

image = cv2.imread(adressOriginalImages + 'vaca3.jpg')

imageAux = copy.copy(image)

imageBlured = cv2.medianBlur(imageAux, 7)
cv2.imwrite('imageBlured' + str((i+1)) + '.bmp', imageBlured)

imageEdges = cv2.Canny(imageBlured, 75, 125, L2gradient=True)
imageEdges = cv2.bitwise_not(imageEdges) # inverto as linhas de branco para preto e o fundo de preto para branco
cv2.imwrite('imageEdges' + str((i+1)) + '.bmp', imageEdges)

imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB) # faço a img ter 3 canais novamente

imageFiltered = cv2.bilateralFilter(imageBlured, 5, 150, 150)
cv2.imwrite('imageFiltered' + str((i+1)) + '.bmp', imageFiltered)

imageKmeans = imageFiltered.reshape((-1, 3))
imageKmeans = np.float32(imageKmeans)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
k = 24

_ret, _label, _center = cv2.kmeans(imageKmeans, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

_center = np.uint8(_center)
_res = _center[_label.flatten()]
_res2 = _res.reshape(imageAux.shape)
cv2.imwrite('res2' + str((i+1)) + '.bmp', _res2)

imageCartoon = cv2.bitwise_and(_res2, imageEdges)
cv2.imwrite('imageCartoon' + str((i+1)) + '.bmp', imageCartoon)