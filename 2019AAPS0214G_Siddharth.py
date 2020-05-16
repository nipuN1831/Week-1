import numpy as np
from PIL import Image,ImageOps
img = Image.open("D:/PythonNumpyAssignmentImage.jpg")
#print(img)
arr = np.array(img)
#print(arr)
#Inverting
for i in range(len(arr)):
    arr[i] = 255-arr[i]
im = Image.fromarray(arr)
im.show()
#Found this one line code too- im_invert = ImageOps.invert(im)
#im_invert.show()
