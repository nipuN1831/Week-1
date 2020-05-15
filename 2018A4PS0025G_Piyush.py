import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
im = Image.open(r'D:\Downloads\np_img.jpg')
im1 = im.convert('1')   #Grayscale image
a = np.asarray(im)      #Array from image
b = Image.fromarray(a) #Image from array
c = np.asarray(im1)
Image.fromarray(a).save('D:\Downloads\A1.jpg') # Saving image from array

