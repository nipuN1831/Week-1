from PIL import Image
import numpy as np 

img=Image.open('marbles.jpg')
img_py=np.array(img)