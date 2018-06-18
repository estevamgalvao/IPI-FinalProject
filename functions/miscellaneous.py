import os

def confirmDir(adressOI = './images/originalImages/', adressTI = './images/toonifyImages/', profile = 0):
    if profile == 0:
        adressOriginalImages = './images/originalImages/'
        adressToonifyImages = './images/toonifyImages/'
        adressBluredImages = './images/bluredImages/'
        adressEdgesImages = './images/edgesImages/'
        adressbFilteredImages = './images/bFilteredImages/'
        adressQuantizedImages = './images/quantizedImages/'
        adresses = [adressOriginalImages, adressToonifyImages, adressBluredImages, adressEdgesImages, adressbFilteredImages, adressQuantizedImages]
        for adress in (adresses[1:]):
            if not os.path.exists(adress):
                os.makedirs(adress)
        return adresses
    else:
        adressOriginalImages = adressOI
        adressToonifyImages = adressTI
        adresses = [adressOriginalImages, adressToonifyImages]
        for adress in (adresses[1:]):
            if not os.path.exists(adress):
                os.makedirs(adress)
        return adresses

def confirmProfile(profile):
    if profile == 0:
        print("\nWelcome, Admin.\n")
        adresses = confirmDir()
    elif profile == 1:
        adressOI = input("Orignal image folder:\n")
        adressTI = input("Toonified image folder:\n")
        adresses = confirmDir(adressOI, adressTI, profile)
    else:
        print("Invalid option.\nYou're a user.")
        adressOI = input("Image folder:\n")
        adressTI = input("Toonified image folder:\n")
        confirmDir(adressOI, adressTI, profile)
        adresses = confirmDir(adressOI, adressTI, profile)
    return adresses