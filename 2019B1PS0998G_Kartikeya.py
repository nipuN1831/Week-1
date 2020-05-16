import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('image.jpg')
img.show()
img_array = np.array(img)
print(img_array)

inv_array = 25 - img_array
print(inv_array)
inv_img = Image.fromarray(inv_array)
inv_img.show()
inv_img.save("Inverted.jpg")

img_Gscale = img.convert('LA')
img_Gscale.show()
