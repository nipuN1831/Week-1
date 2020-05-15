from PIL import Image
import numpy

# IMAGE WITH INVERTED COLOUR
im = Image.open("abc.jpg")
arr = numpy.array(im)
Arr = 255 - arr
Image.fromarray(Arr).save(
    "/Users/vishaltyagi/Documents/ARJUN/COLLEGE/CODING/PYTHON/INVERTED.jpg")


# IMAGE IN GRAYSCALE
N, M, P = numpy.shape(arr)
i = j = 0
for i in range(N):
    for j in range(M):
        arr[i, j] = 0.2125 * arr[i, j, 0] + 0.7154 * \
            arr[i, j, 1] + 0.0721 * arr[i, j, 2]
Image.fromarray(arr).save(
    "/Users/vishaltyagi/Documents/ARJUN/COLLEGE/CODING/PYTHON/GRAYSCALE.jpg")
