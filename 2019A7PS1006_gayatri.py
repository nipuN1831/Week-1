import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import io
photo=io.imread('trial1.jpg')
a=np.ones(photo.shape)
b=np.multiply(a,250)
c=np.subtract(b,photo)
img=Image.fromarray(c,'RGB')
img.save('trial2.png')