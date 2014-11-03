from PIL import Image

def plot_hist(img):
    width, height = img.size
    frequencies = getGrayFrequencies(img)
    total = width * height + 0.0
    for gray in frequencies:
        gray["pr"] = gray["count"] / total
    plot(frequencies)

def plot(grayData):
    print grayData


def getGrayFrequencies(img):
    levels = [dict(count=0) for x in xrange(0, 256)]
    width, height = img.size
    for x in xrange(width):
        for y in xrange(height):
            gray = img.getpixel((x, y))
            levels[gray]["count"] += 1
    return levels

if __name__ == "__main__":
    img = Image.open("49.png")
    plot_hist(img)
