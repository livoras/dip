from PIL import Image

def quantization(input_image, level):
    output_image = Image.new(input_image.mode, input_image.size)
    width, height = input_image.size
    for x in xrange(width):
        for y in xrange(height):

            pi = input_image.getpixel((x, y))
            gap = 256 / level # 一个层次有多少个像素
            color_stop = 255.0 / (level - 1) # 一个层次的颜色跨度
            target_pi = int(pi / gap * color_stop) # 算出该像素颜色对应的层次的颜色
            output_image.putpixel((x, y), target_pi) # 覆盖原来的颜色

    return output_image

def quantization_save(input_image, level):
    new_image = quantization(input_image, level)
    new_image.save("level-%s.png" % (level))

if __name__ == "__main__":
    img = Image.open("./49.png")
    quantization_save(img, 128)
    quantization_save(img, 32)
    quantization_save(img, 8)
    quantization_save(img, 4)
    quantization_save(img, 2)
