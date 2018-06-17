import cv2
import copy
import numpy as np
import glob
import datetime

adressOriginalImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/originalImages/'
adressBluredImages    = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bluredImages/'
adressEdgesImages     = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/edgesImages/'
adressbFilteredImages = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bFilteredImages/'
adressRes2Images      = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/res2Images/'
adressCartoonImages   = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/cartoonImages/'


typeImage = '*.jpg'
adressOriginalImages += typeImage
originalImagesArray = [cv2.imread(file) for file in glob.glob(adressOriginalImages)]

a = datetime.datetime.now()
for i in range(len(originalImagesArray)):
    imageAux = copy.copy(originalImagesArray[i])

    imageBlured = cv2.medianBlur(imageAux, 7)
    cv2.imwrite(adressBluredImages + 'imageBlured' + str((i+1)) + '.bmp', imageBlured)

    imageEdges = cv2.Canny(imageBlured, 75, 125, L2gradient=True)
    imageEdges = cv2.bitwise_not(imageEdges) # inverto as linhas de branco para preto e o fundo de preto para branco
    cv2.imwrite(adressEdgesImages + 'imageEdges' + str((i+1)) + '.bmp', imageEdges)

    imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB) # faço a img ter 3 canais novamente

    imageFiltered = cv2.bilateralFilter(imageBlured, 5, 150, 150)
    cv2.imwrite(adressbFilteredImages + 'imageFiltered' + str((i+1)) + '.bmp', imageFiltered)

    imageKmeans = imageFiltered.reshape((-1, 3))
    imageKmeans = np.float32(imageKmeans)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
    k = 24

    _ret, _label, _center = cv2.kmeans(imageKmeans, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    _center = np.uint8(_center)
    _res = _center[_label.flatten()]
    _res2 = _res.reshape(originalImagesArray[i].shape)
    cv2.imwrite(adressRes2Images + 'res2' + str((i+1)) + '.bmp', _res2)

    imageCartoon = cv2.bitwise_and(_res2, imageEdges)
    cv2.imwrite(adressCartoonImages + 'imageCartoon' + str((i+1)) + '.bmp', imageCartoon)
b = datetime.datetime.now()
print("\nThe program took %d hours, %d minutes and %d seconds to execute"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))
