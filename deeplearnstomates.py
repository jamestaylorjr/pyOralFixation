#importing the required libraries
import numpy as np
import os
import skimage
from skimage import img_as_ubyte
from skimage.io import imread, imshow, imsave
from skimage.data import camera, img_as_bool
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
%matplotlib inline

trainingimages = []

for image in os.listdir():
  if image.endswith(".png"):
    trainingimages.append(image)


#reading the image 
for image in trainingimages:
  read_image = imread(image, as_gray=True)
  roberts_image = roberts(read_image)
  roberts_image_ubyte = img_as_ubyte(roberts_image)
  imsave(image + "_roberts.png", roberts_image_ubyte)
  # imshow(image, cmap=plt.cm.gray)
  # plt.tight_layout()
  # plt.show()


# trainingimages = []

# for image in os.listdir():
#   if image.endswith("roberts.png"):
#     os.remove(image)
