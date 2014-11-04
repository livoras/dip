from PIL import Image
from averaging_filters import averaging_filter
from laplacian_filter import laplacian_filter
from sobel_filter import sobel_filter

def filter2d(img, filterName, size=None, sobelType=1):
    if filterName == "averaging":
        return averaging_filter(img, size)
    elif filterName == "laplacian":
        return laplacian_filter(img)
    elif filterName == "sobel":
        return sobel_filter(img, sobelType)

if __name__ == "__main__":
    img = Image.open("49.png")

    # Test for averaging filter
    newImg = filter2d(img, "averaging", size=(3, 3))
    newImg.save("averaging_filters_results/3x3.png")

    newImg = filter2d(img, "averaging", size=(7, 7))
    newImg.save("averaging_filters_results/7x7.png")

    newImg = filter2d(img, "averaging", size=(11, 11))
    newImg.save("averaging_filters_results/11x11.png")

    # Test for laplacian filter
    newImg = filter2d(img, "laplacian")
    newImg.save("laplacian_filter_results/3x3.png")

    # Test for sobel filter
    newImg = filter2d(img, "sobel", sobelType=1)
    newImg.save("sobel_filter_results/filter_1.png")

    newImg = filter2d(img, "sobel", sobelType=2)
    newImg.save("sobel_filter_results/filter_2.png")
