import numpy as np

def cannyThreshold(image, sigma=0.77):
    median = np.median(image)

    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))

    return [lower, upper]