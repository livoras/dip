from PIL import Image

def sobel_filter(img, sobelType):
    width, height = img.size
    newImg = img.copy()

    def makeSobel1(x, y):

        value = getPix(x - 1, y - 1) * -1
        value = value + getPix(x, y - 1) * -2
        value = value + getPix(x + 1, y - 1) * -1

        value = value + getPix(x - 1, y + 1) * 1
        value = value + getPix(x, y + 1) * 2
        value = value + getPix(x + 1, y + 1) * 1

        newImg.putpixel((x, y), value)

    def makeSobel2(x, y):

        value = getPix(x - 1, y - 1) * -1
        value = value + getPix(x - 1, y) * -2
        value = value + getPix(x - 1, y + 1) * -1

        value = value + getPix(x + 1, y - 1) * 1
        value = value + getPix(x + 1, y) * 2
        value = value + getPix(x + 1, y + 1) * 1

        newImg.putpixel((x, y), value)

    def getPix(x, y):
        try:
            pix = img.getpixel((x, y))
        except:
            pix = 0
        return pix

    for x in xrange(width):
        for y in xrange(height):
            if sobelType == 1: makeSobel1(x, y)
            elif sobelType == 2: makeSobel2(x, y)

    return newImg


if __name__ == "__main__":
    img = Image.open("49.png")

    newImg = sobel_filter(img, 1)
    newImg.save("sobel_filter_results/filter_1.png")

    newImg = sobel_filter(img, 2)
    newImg.save("sobel_filter_results/filter_2.png")
