from PIL import Image

def averaging_filter(img, size):
    w, h = size
    h_pixs, v_pixs = w / 2, h / 2
    width, height = img.size
    totalPixelsInFilter = w * h
    newImg = img.copy()

    def makeAverage(x, y):
        total = 0
        for innerX in xrange(x - h_pixs, x + h_pixs + 1):
            for innerY in xrange(y - v_pixs, y + v_pixs + 1):
                try:
                    pix = img.getpixel((innerX, innerY))
                except:
                    pix = 0
                total += pix
        newImg.putpixel((x, y), total / totalPixelsInFilter)

    for x in xrange(width):
        for y in xrange(height):
            makeAverage(x, y)

    return newImg


if __name__ == "__main__":
    img = Image.open("49.png")

    newImg = averaging_filter(img, (3, 3))
    newImg.save("averaging_filters_results/3x3.png")

    newImg = averaging_filter(img, (7, 7))
    newImg.save("averaging_filters_results/7x7.png")

    newImg = averaging_filter(img, (11, 11))
    newImg.save("averaging_filters_results/11x11.png")
