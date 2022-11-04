import cv2
import matplotlib.pyplot as plt
from filters import RedBlueImageFilterRGB, RedBlueImageFilterHSV

# Imagename Input by user and reading the image as "color"

imginput = str(input("Please enter the entire filename (including .jpg, .png etc.): "))
img = cv2.imread(imginput)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image', img)

#
rbfilter = RedBlueImageFilterRGB(img=img)
cv2.imshow('Edited Image using RGB', rbfilter)
    
# Window Closing stuff

print("Close the Window by pressing any key")
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the Image

# cv2.imwrite("result.jpg", img)