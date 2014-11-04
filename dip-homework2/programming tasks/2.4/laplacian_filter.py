from PIL import Image

def laplacian_filter(img):
    w, h = 3, 3
    h_pixs, v_pixs = w / 2, h / 2
    width, height = img.size
    newImg = img.copy()

    def makeLaplacian(x, y):
        total = 0
        # 遍历某个元素附近的像素点，统计所有边缘像素的和
        for innerX in xrange(x - h_pixs, x + h_pixs + 1):
            for innerY in xrange(y - v_pixs, y + v_pixs + 1):
                # 本元素不参与计算
                if innerX == x and innerY == y: continue
                try:
                    pix = img.getpixel((innerX, innerY))
                except:
                    pix = 0
                total += pix
        # 使用书本上第二个Laplacian算子对像素值进行计算和写入
        newImg.putpixel((x, y), total - 8 * img.getpixel((x, y)))

    for x in xrange(width):
        for y in xrange(height):
            makeLaplacian(x, y)

    return newImg


if __name__ == "__main__":
    img = Image.open("49.png")

    newImg = laplacian_filter(img)
    newImg.save("laplacian_filter_results/3x3.png")
