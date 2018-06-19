import cv2
import glob
import numpy as np
import datetime

from functions.miscellaneous import *

profile = int(input("- Profiles -\n[0] Admin\n[1] User\nselect: "))
adresses = confirmProfile(profile)
typeImage = input("Image type:\n")
typeImage = '*.' + typeImage
# print(adresses)
# print(adresses[0] + typeImage)
originalImagesArray = [cv2.imread(file) for file in sorted(glob.glob(adresses[0] + typeImage))]
# print((len(originalImagesArray)))
typeImage = typeImage[1:]

print("\n- Toonifying -\n")
a = datetime.datetime.now()
bigImage = 0
for index in range(len(originalImagesArray)):
    print(str((index + 1)) + 'º Image processing...')
    imageAux = originalImagesArray[index]
    image = originalImagesArray[index]
    height, width = image.shape[:2]

    # Se a imagem for além de FULL HD - 1920x1080 - #
    if height * width > 2073600:
        bigImage = 1
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
    ret, label, center = cv2.kmeans(imageKmeans, kClusters, None, quantizationCriteria, 10,
                                       cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    outputAux = center[label.flatten()]
    imageQuantized = outputAux.reshape(imageAux.shape)

    # Recombino a imagem quantizada com as bordas da imagem borrada #
    imageToonify = cv2.bitwise_and(imageQuantized, imageEdges)

    if profile == 0:
        cv2.imwrite(adresses[2] + 'blured' + str((index + 1)) + typeImage, imageBlured)
        cv2.imwrite(adresses[3] + 'edges' + str((index + 1)) + typeImage, imageEdges)
        cv2.imwrite(adresses[4] + 'filtered' + str((index + 1)) + typeImage, imageFiltered)
        cv2.imwrite(adresses[5] + 'quantized' + str((index + 1)) + typeImage, imageQuantized)
    cv2.imwrite(adresses[1] + 'toonify' + str((index + 1)) + typeImage, imageToonify)
b = datetime.datetime.now()

print("\nSuccess! Images were created.")
print("The program took %d hours, %d minutes and %d seconds to execute"%(abs(b.hour-a.hour), abs(b.minute-a.minute), abs(b.second-a.second)))