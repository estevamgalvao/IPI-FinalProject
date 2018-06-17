import numpy as np

def RGB_YCbCr(img, option = 1):
    height, width, channels = img.shape

    if (option == 1):
        imageY = np.zeros((height, width), dtype=np.int8)
        imageCb = np.zeros((height, width), dtype=np.int8)
        imageCr = np.zeros((height, width), dtype=np.int8)

        imageY = (0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2])
        imageCr = (0.713 * img[:, :, 2] - 0.713 * imageY + 128)
        imageCb = (0.564 * img[:, :, 0] - 0.564 * imageY + 128)

        img[:, :, 0] = imageY
        img[:, :, 1] = imageCr
        img[:, :, 2] = imageCb

    elif (option == 2):

        imageR = np.zeros((height, width), dtype=np.int8)
        imageG = np.zeros((height, width), dtype=np.int8)
        imageB = np.zeros((height, width), dtype=np.int8)

        imageR = img[:, :, 0] + (1.402 * img[:, :, 1] - 1.402 * 128)
        imageG = img[:, :, 0] + (-0.714 * img[:, :, 1] - (-0.714 * 128)) + (-0.344 * img[:, :, 2] - (-0.344 * 128))
        imageB = img[:, :, 0] + (1.772 * img[:, :, 2] - 1.772 * 128)

        img[:, :, 0] = imageB
        img[:, :, 1] = imageG
        img[:, :, 2] = imageR

    else:
        print("não fode, moai")
