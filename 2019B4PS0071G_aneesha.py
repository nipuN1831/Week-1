from PIL import Image
import numpy
a = Image.open("/home/aneesha/Downloads/a.jpg")
ar = numpy.array(a)
Ar = 255 - ar
Image.fromarray(Ar).show()
rgb = [0.2989, 0.5870, 0.1140]
grayscale_im = numpy.dot(ar, rgb)
Image.fromarray(grayscale_im).show()
