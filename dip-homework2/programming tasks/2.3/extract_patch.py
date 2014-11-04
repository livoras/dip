from random import randint
from PIL import Image

def view_as_window(img, patch_size, folder, getAll=False):
    w, h = patch_size
    width, height = img.size
    xBound = width - w
    yBound = height - h

    def extractAll():
        count = 0
        for x in xrange(xBound):
            for y in xrange(yBound):
                count += 1
                makePatch(img, (x, y), (w, h), folder, count)

    def random8():
        count = 8
        while (count != 0):
            x = randint(0, xBound)
            y = randint(0, yBound)
            makePatch(img, (x, y), (w, h), folder, count)
            count -= 1

    if getAll: extractAll()
    else: random8()

def makePatch(img, pos, size, folder, count):
    x, y = pos
    w, h = size
    left = x
    upper = y
    right = x + w
    lower = y + h
    patch = img.crop((left, upper, right, lower))
    patch.save("%s/%s.png" % (folder, count))

if __name__ == "__main__":
    img = Image.open("49.png")
    view_as_window(img, (96, 64), "96x64")
    view_as_window(img, (50, 50), "50x50")
