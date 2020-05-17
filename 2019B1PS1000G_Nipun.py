import numpy as np
from PIL import Image

im = np.array(Image.open('d:\QSTP\Assign.jpg'))

im_i = 255 - im

Image.fromarray(im_i).save('d:\QSTP\Hello\Assign_inv.jpg')
