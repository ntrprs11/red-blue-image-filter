from copy import copy
import cv2

def RedBlueImageFilterRGB(img):
    """red blue image filter using rgb editing"""
    rb = copy(img)
    x_size = img.shape[0]
    y_size = img.shape[1]
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for i in range(x_size):
        for j in range(y_size):
            rb[i][j][0] = int((img[i][j][0] / 255) * 100)# red
            rb[i][j][1] = int((img[i][j][1] / 255) * 40) # green
            rb[i][j][2] = int((img[i][j][2] / 255) * 200)# blue
    return rb


def RedBlueImageFilterHSV(img):
    """red blue image filter using hsv editing"""