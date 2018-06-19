import cv2
import copy
import numpy as np
import glob
import datetime

adressOriginalImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/originalImages/'
adressBluredImages    = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bluredImages/'
adressEdgesImages     = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/edgesImages/'
adressbFilteredImages = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/bFilteredImages/'
adressRes2Images      = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/quantizedImages/'
adressCartoonImages   = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/cartoonImages/'
adressAuxImages  = '/home/estevamgalvao/Documentos/PycharmProjects/IPI-FinalProject/images/auxImages/'

typeImage = '*.jpg'
# adressOriginalImages += typeImage
originalImagesArray = [cv2.imread(file) for file in sorted(glob.glob(adressOriginalImages + typeImage))]
# print(originalImagesArray)
# imagem = cv2.imread(adressOriginalImages + 'vaca3.jpg')
# imagem2 = originalImagesArray[8]
# cv2.imshow('vaca3', imagem)
# cv2.waitKey(0)
# cv2.imshow('vacaarray', imagem2)
# cv2.waitKey(0)

# parece que o glob tá mudando de alguma forma a res2 da img
typeImage = typeImage[1:]
a = datetime.datetime.now()
numImages = len(originalImagesArray)
# numImages = 1
for i in range(numImages):

    imageAux = originalImagesArray[i]
    cv2.imwrite(adressAuxImages + 'imageAux' + str((i+1)) + typeImage, imageAux)
    # imageAux = cv2.imread(adressOriginalImages + 'img' + str((i + 1)) + '.jpg')
    print(adressOriginalImages + 'img' + str((i + 1)) + '.jpg')

    imageBlured = cv2.medianBlur(imageAux, 7)
    cv2.imwrite(adressBluredImages + 'imageBlured' + str((i+1)) + typeImage, imageBlured)
    # cv2.imwrite(adressBluredImages + 'SEMGLOBimageBlured' + str((i+1)) + typeImage, imageBlured)


    imageEdges = cv2.Canny(imageBlured, 62.5, 125, L2gradient=True)
    imageEdges = cv2.bitwise_not(imageEdges) # inverto as linhas de branco para preto e o fundo de preto para branco
    cv2.imwrite(adressEdgesImages + 'imageEdges' + str((i+1)) + typeImage, imageEdges)
    # cv2.imwrite(adressEdgesImages + 'SEMGLOBimageEdges' + str((i+1)) + typeImage, imageEdges)

    imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB) # faço a img ter 3 canais novamente

    imageFiltered = cv2.bilateralFilter(imageBlured, 7, 35, 35)
    cv2.imwrite(adressbFilteredImages + 'imageFiltered' + str((i+1)) + typeImage, imageFiltered)
    # cv2.imwrite(adressbFilteredImages + 'SEMGLOBimageFiltered' + str((i+1)) + typeImage, imageFiltered)


    imageKmeans = imageFiltered.reshape((-1, 3))
    imageKmeans = np.float32(imageKmeans)
    quantizationCriteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
    kClusters = 24

    _ret, _label, _center = cv2.kmeans(imageKmeans, kClusters, None, quantizationCriteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    _center = np.uint8(_center)
    _res = _center[_label.flatten()]
    imageQuantized = _res.reshape(imageAux.shape)
    cv2.imwrite(adressRes2Images + 'imageQuantized' + str((i+1)) + typeImage, imageQuantized)
    # cv2.imwrite(adressRes2Images + 'SEMGLOBimageQuantized' + str((i+1)) + typeImage, imageQuantized)

    imageCartoon = cv2.bitwise_and(imageQuantized, imageEdges)
    cv2.imwrite(adressCartoonImages + 'imageCartoon' + str((i+1)) + typeImage, imageCartoon)
    # cv2.imwrite(adressCartoonImages + 'SEMGLOBimageCartoon' + str((i+1)) + typeImage, imageCartoon)

b = datetime.datetime.now()
print("\nThe program took %d hours, %d minutes and %d seconds to execute"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))
