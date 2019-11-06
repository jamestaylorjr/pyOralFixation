#just some utility code blocks for slicing up images, will format later

import image_slicer
import os
import PIL
from PIL import Image



cwd = os.getcwd()
trainingimages = []
trainingdataset = []

# for cwdfile in os.listdir():
#     if cwdfile.startswith("training"):
#         os.rename(cwdfile, cwdfile + ".png")

# counter = 1
# counter2 = 1
# for cwdfile in os.listdir():
#     if cwdfile.endswith('.jpg'):
#         os.rename(cwdfile, "xtraining" + str(counter))
#         counter = counter+1
#     else:
#         if cwdfile.endswith(".png"):
#             os.rename(cwdfile, "training" + str(counter2))
#             counter2 = counter2 + 1



# for cwdfile in os.listdir():
#     if cwdfile.endswith('.jpg'):
#         if cwdfile.startswith('training'):
#             trainingimages.append(cwdfile)


# for trainingimg in trainingimages:
#          image_slicer.slice(trainingimg, 60)

