from Bia import *
import random
import json
import numpy as np
from PIL import Image

import cv2 as cv
from matplotlib import pyplot as plt

f = open("database/images.json","r")

database = json.loads(f.read())
database = list(database.values())[2]
f.close()

size = database["size"]
images_json = database["images"]
data = np.array(images_json[0]["image"]).astype("uint8")

im = cv.imread('/Users/samuelbrasileiro/Desktop/euu.png')
# data = np.array([np.concatenate(column) for column in data])
gray = cv.cvtColor(data, cv2.COLOR_RGB2GRAY)


dft = cv.dft(np.float32(gray),flags = cv.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


rows, cols = gray.shape
crow,ccol = int(rows/2) , int(cols/2)
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)

r_out = 100
r_in = 20

x, y = np.ogrid[:rows, :cols]
mask_area = np.logical_and(((x - crow) ** 2 + (y - ccol) ** 2 >= r_in ** 2), ((x - crow) ** 2 + (y - ccol) ** 2 <= r_out ** 2))
mask[mask_area] = 1
#


# apply mask and inverse DFT
fshift = dft_shift*mask

fshift_mask_mag = 20*np.log(cv.magnitude(fshift[:,:,0],fshift[:,:,1]))


f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(221),plt.imshow(gray, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Initial Magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_back, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(fshift_mask_mag, cmap = 'gray')
plt.title('Final Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()



# img = Image.fromarray(data.astype("uint8"), mode='RGB')


# img.show()

# [233, 122,   1,  12, 101, 201, 200, 155,
#  123,   2,   2, 222,  21, 223, 176, 133,
#  233, 122,   1,  12, 101, 201, 200, 155,
#  123,   2,   2, 222,  21, 223, 176, 133,
#  233, 122,   1,  12, 101, 201, 200, 155,
#  123,   2,   2, 222,  21, 223, 176, 133,
#  233, 122,   1,  12, 101, 201, 200, 155,
#  123,   2,   2, 222,  21, 223, 176, 133]

# [  1,   1,   1,   1,   1,   1,   1,   1,
#    1,   1,   1,   1,   1,   1,   1,   1,
#    1,   1,   0,   0,   0,   0,   1,   1,
#    1,   1,   0,   0,   0,   0,   1,   1,
#    1,   1,   0,   0,   0,   0,   1,   1,
#    1,   1,   0,   0,   0,   0,   1,   1,
#    1,   1,   1,   1,   1,   1,   1,   1,
#    1,   1,   1,   1,   1,   1,   1,   1]