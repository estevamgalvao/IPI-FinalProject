import numpy as np

def cannyThreshold(image, sigma=0.77):
    # compute the median of the single channel pixel intensities
    median = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))

    return [lower, upper]