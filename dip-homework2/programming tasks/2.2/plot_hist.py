import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import normal
from matplotlib.ticker import FuncFormatter
from PIL import Image

def plot_hist(img):
    width, height = img.size
    frequencies, pixels = getGrayFrequencies(img)
    total = width * height + 0.0
    for gray in frequencies:
        gray["pr"] = gray["count"] / total
    plot(pixels)

def plot(pixels):
    plt.title("Histogram of Gray")
    plt.xlabel("Gray")
    plt.ylabel("Probability")
    plt.hist(pixels, bins=256, normed=True)
    plt.show()

def getGrayFrequencies(img):
    levels = [dict(count=0) for x in xrange(0, 256)]
    width, height = img.size
    pixels = []
    for x in xrange(width):
        for y in xrange(height):
            gray = img.getpixel((x, y))
            pixels.append(gray)
            levels[gray]["count"] += 1
    return levels, pixels

if __name__ == "__main__":
    img = Image.open("49.png")
    plot_hist(img)
