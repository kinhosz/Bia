from Bia import *
import random
import json
import numpy as np
from PIL import Image

import cv2 as cv
from matplotlib import pyplot as plt
f = open("database/images.json","r")

database = json.loads(f.read())
database = list(database.values())[0]
f.close()

size = database["size"]
images_json = database["images"]
data = np.array(images_json[0]["image"]).astype("uint8")

# data = np.array([np.concatenate(column) for column in data])
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)

dft = cv.dft(np.float32(gray),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(gray, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


img = Image.fromarray(data.astype("uint8"), mode='RGB')


img.show()

