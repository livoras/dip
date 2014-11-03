from PIL import Image
from os import path

def scale(input_img, size):
    """
        :: Nearsest Neighbor Algorithm
    """
    output_img = Image.new(input_img.mode, size)
    origin_width, origin_height = input_img.size
    target_width, target_height = output_img.size
    for i in xrange(0, target_height):
        for j in xrange(0, target_width):
            cp_i = int(float(i) / target_height * origin_height)
            cp_j = int(float(j) / target_width * origin_width)
            output_img.putpixel((j, i), input_img.getpixel((cp_j, cp_i)))
    return output_img

def scale_save(img, size):
    new_img = scale(img, size)
    new_img.save("./%dx%d.png" % size)

if __name__ == "__main__":
    img = Image.open("./49.png")
    scale_save(img, (192, 128))
    scale_save(img, (96, 64))
    scale_save(img, (48, 32))
    scale_save(img, (24, 16))
    scale_save(img, (12, 8))

    scale_save(img, (300, 200))
    scale_save(img, (450, 300))
    scale_save(img, (500, 200))
