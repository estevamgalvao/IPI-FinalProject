import cv2
import glob
import numpy as np
import datetime
import os
from functions.miscellaneous import *


adressOriginalImages = './images/4kimages/originalImages/'
adressToonifyImages = './images/4kimages/toonifyImages/'
adressBluredImages = './images/4kimages/bluredImages/'
adressEdgesImages = './images/4kimages/edgesImages/'
adressbFilteredImages = './images/4kimages/bFilteredImages/'
adressQuantizedImages = './images/4kimages/quantizedImages/'

adresses = [adressOriginalImages, adressToonifyImages, adressBluredImages, adressEdgesImages, adressbFilteredImages,
            adressQuantizedImages]

for adress in (adresses[1:]):
    if not os.path.exists(adress):
        os.makedirs(adress)


typeImage = 'jpg'
typeImage = '*.' + typeImage
originalImagesArray = [cv2.imread(file) for file in sorted(glob.glob(adresses[0] + typeImage))]
typeImage = typeImage[1:]

a = datetime.datetime.now()
bigImage = 0
profile = 0
for index in range(len(originalImagesArray)):
    print(str((index + 1)) + 'º Image processing...')
    imageAux = originalImagesArray[index]
    image = originalImagesArray[index]
    height, width, channels = image.shape

    # Se a imagem for além de FULL HD - 1920x1080 - #
    if height * width > 2073600:
        bigImage = 1
        print(bigImage)
        image = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    # Suavizo a imagem para reduzir ruídos e capturar suas bordas em seguida #
    imageBlured = cv2.medianBlur(image, 7)

    # Capturo as bordas da imagem, as transformo de preto para branco e as faço ser RGB (ter 3 canais de cores) #
    imageEdges = cv2.Canny(imageBlured, 62.5, 125, L2gradient=True)
    imageEdges = cv2.bitwise_not(imageEdges)
    imageEdges = cv2.cvtColor(imageEdges, cv2.COLOR_GRAY2RGB)

    # Aplico um filtro bilateral para suavizar os detalhes na imagem #
    imageFiltered = cv2.bilateralFilter(imageBlured, 7, 35, 35)

    if bigImage == 1:
        imageEdges = cv2.resize(imageEdges, (width, height), interpolation=cv2.INTER_CUBIC)
        imageFiltered = cv2.resize(imageFiltered, (width, height), interpolation=cv2.INTER_CUBIC)

    # Início da quantização das cores #
    imageKmeans = imageFiltered.reshape((-1, 3))
    imageKmeans = np.float32(imageKmeans)
    # Defino um critério de parada para o algoritmo Kmeans. Ou são feitas 10 iterações, ou o episilon 1 é atingido #
    quantizationCriteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
    # Defino a quantidade de clusters para as cores #
    kClusters = 24
    _ret, _label, _center = cv2.kmeans(imageKmeans, kClusters, None, quantizationCriteria, 10,
                                       cv2.KMEANS_RANDOM_CENTERS)
    _center = np.uint8(_center)
    _res = _center[_label.flatten()]
    imageQuantized = _res.reshape(imageAux.shape)

    # Recombino a imagem quantizada com as bordas da imagem borrada #
    imageToonify = cv2.bitwise_and(imageQuantized, imageEdges)

    if profile == 0:
        cv2.imwrite(adresses[2] + 'imageBlured' + str((index + 1)) + typeImage, imageBlured)
        cv2.imwrite(adresses[3] + 'imageEdges' + str((index + 1)) + typeImage, imageEdges)
        cv2.imwrite(adresses[4] + 'imageFiltered' + str((index + 1)) + typeImage, imageFiltered)
        cv2.imwrite(adresses[5] + 'imageQuantized' + str((index + 1)) + typeImage, imageQuantized)
    cv2.imwrite(adresses[1] + 'imageCartoon' + str((index + 1)) + typeImage, imageToonify)
b = datetime.datetime.now()

print("Success! Images were created.")
print("\nThe program took %d hours, %d minutes and %d seconds to execute"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))