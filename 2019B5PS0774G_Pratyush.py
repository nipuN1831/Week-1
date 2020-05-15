from PIL import Image
import numpy as np 
import matplotlib.image as mat_im
import matplotlib.pyplot as mat_plt

img=Image.open('marbles.jpg')       #image located in same place as this file  
img_np=np.array(img)                #idk looked like marbles to me :p

# first method
inv_np = np.invert(img_np)
inv_img = Image.fromarray(inv_np)
inv_img.save("inverted_marbles.jpg")

# second method
inv2_np = 255-img_np
inv2_img = Image.fromarray(inv2_np)
inv2_img.save("inverted_marbles2.jpg")

# greyscale
img_m = mat_im.imread('marbles.jpg')
grey = np.dot(img_m[...,:3], [0.299, 0.587, 0.144])         #don't understand this very well
mat_plt.imshow(grey, cmap = mat_plt.get_cmap('gray'))
mat_plt.savefig('greyscale_marbles.jpg')