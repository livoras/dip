import math

from PIL import Image
from plot_hist import plot_hist, getGrayFrequencies

def equalize_hist(img):
    width, height = img.size
    total = width * height
    grayData, pixels = getGrayFrequencies(img)
    transferedGrays = []
    acc = 0.0
    for gray in grayData:
        acc += gray["count"]
        val = math.floor((acc / total) * 255)
        transferedGrays.append(val)
    return createNewImageWithGrays(img, transferedGrays)

def createNewImageWithGrays(img, transferedGrays):
    newImg = img.copy()
    width, height = newImg.size
    for x in xrange(width):
        for y in xrange(height):
            currentGray = newImg.getpixel((x, y))
            newImg.putpixel((x, y), transferedGrays[currentGray])
    return newImg

if __name__ == "__main__":
    img = Image.open("49.png")
    newImg = equalize_hist(img)
    newImg.save("49_after_equalize_hist.png")
    plot_hist(newImg)