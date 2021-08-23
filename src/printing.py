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
gray = cv2.cvtColor(data, cv2.COLOR_RGB2GRAY)


dft = cv.dft(np.float32(gray),flags = cv.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft)

#primeira parte eh a real e a segunda eh a imaginaria###############################################################
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
r = 10

rows, cols = gray.shape
crow,ccol = int(rows/2) , int(cols/2)
# create a mask first, center square is 1, remaining all zeros
mask = np.ones((rows,cols,2),np.uint8)



############################################################################################
center = [crow,ccol]
x,y = np.ogrid[:rows,:cols]
mask_area = (x-center[0])**2 + (y-center[1])**2 <= r*r
#filtro passa alta, se fosse =1 era passa baixa
mask[mask_area] = 0






fshift = dft_shift*mask
fshift_mask_mag = 20*np.log(cv2.magnitude(fshift[:,:,0],fshift[:,:,1]))
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(gray,cmap = 'gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum, cmap='gray')
ax2.title.set_text('FFT of image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(fshift_mask_mag, cmap='gray')
ax3.title.set_text('FFT + Mask')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_back, cmap='gray')
ax4.title.set_text('After inverse FFT')
plt.show()




'''

spc = 80

# mask[crow-spc:crow+spc+1, ccol-spc:ccol+spc+1] = 0
# print(mask)

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(gray, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()



# img = Image.fromarray(data.astype("uint8"), mode='RGB')


# img.show()
'''