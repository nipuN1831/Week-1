import numpy as np
import urllib
import PIL
from PIL import Image

img_url = 'https://images-na.ssl-images-amazon.com/images/I/81KA4Aty8xL._SL1000_.jpg'
img_path = '/home/user/Pictures/image.jpg'
invert_img_path = '/home/user/Pictures/invert_image.jpg'
grayscale_img_path = '/home/user/Pictures/grayscale_image.jpg'

urllib.urlretrieve(img_url, img_path)
img = PIL.Image.open(img_path)
img_arr = np.array(img)
invert_img_arr = np.zeros(img_arr.shape, dtype=np.uint8)
grayscale_img_arr = np.zeros(img_arr.shape, dtype=np.uint8)

for i in range(1000):
    for j in range(1000):
        for k in range(3):
            invert_img_arr[i][j][k] = int(255 - img_arr[i][j][k])

invert_img = PIL.Image.fromarray(invert_img_arr, 'RGB')
invert_img.save(invert_img_path)

for i in range(1000):
    for j in range(1000):
        for k in range(3):
            grayscale_img_arr[i][j][k] = 0.2989 * img_arr[i][j][0] + 0.5870 * img_arr[i][j][1] + 0.1140 * img_arr[i][j][2]
    
grayscale_img = PIL.Image.fromarray(grayscale_img_arr, 'RGB')
grayscale_img.save(grayscale_img_path)

# img.show()
# invert_img.show()
# grayscale_img.show()