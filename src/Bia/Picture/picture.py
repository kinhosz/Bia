from PIL import ImageTk, Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class Picture():

    def __init__(self, data):
        self.__data = data
        self.__height = len(data)
        self.__grayImage = []
        self.__grayData = []
        
        if self.__height == 0:
            self.__width = 0
        else:
            self.__width = len(data[0])

        self.__image = None
        self.__side = 300

    def imageSegmentation(self):
        
        gray = cv.cvtColor(self.__data.astype("uint8"), cv.COLOR_RGB2GRAY)
        gray = cv.GaussianBlur(gray, (3,3), 0, 0, cv.BORDER_DEFAULT)

        dft = cv.dft(np.float32(gray),flags = cv.DFT_COMPLEX_OUTPUT)

        dft_shift = np.fft.fftshift(dft)
        #dft_shift = cv2.GaussianBlur(dft_shift, (3, 1), 7)


        magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


        rows, cols = gray.shape
        crow,ccol = int(rows/2) , int(cols/2)
        # create a mask first, center square is 1, remaining all zeros
        mask = np.zeros((rows,cols,2),np.uint8)

        r_out = 180
        r_in = 25

        x, y = np.ogrid[:rows, :cols]
        mask_area = np.logical_and(((x - crow) ** 2 + (y - ccol) ** 2 >= r_in ** 2), ((x - crow) ** 2 + (y - ccol) ** 2 <= r_out ** 2))
        mask[mask_area] = 1
        #


        # apply mask and inverse DFT
        fshift = dft_shift*mask

        fshift_mask_mag = 20*np.log(cv.magnitude(fshift[:,:,0],fshift[:,:,1]))

        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv.idft(f_ishift,flags = cv.DFT_COMPLEX_OUTPUT)
        img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

        return self.__convertTo255(img_back)

    def __convertTo255(self, img, magnitude=1e6):

        maxi = -1

        len_x = len(img)
        len_y = len(img[0])

        for i in range(len_x):
            for j in range(len_y):
                if maxi == -1:
                    maxi = img[i][j]
                maxi = max(maxi, img[i][j])
        
        mini = magnitude
        maxi = maxi - mini
        for i in range(len_x):
            for j in range(len_y):
                img[i][j] = max(img[i][j] - mini,0)
                img[i][j] = min(((img[i][j]/maxi) * 255),255)
        
        return img.astype("uint8")         
        
    def drawSquare(self, side=300):

        HEIGHT = self.__height
        WIDTH = self.__width
        img = self.__data
        self.__side = side

        point1 = (HEIGHT - side)//2 - 1
        point2 = HEIGHT - (HEIGHT - side)//2
        point3 = (WIDTH - side)//2 - 1
        point4 = WIDTH - (WIDTH - side)//2

        for i in range(point1, point2+1):
            img[i][point3] = (0,255,0)
            img[i][point4] = (0,255,0)
        
        for j in range(point3, point4):
            img[point1][j] = (0,255,0)
            img[point2][j] = (0,255,0)

    def mirror(self):

        img = self.__data

        for i in range(self.__height):
            aux = img[i]
            img[i] = aux[::-1]

    def paint(self):

        HEIGHT = self.__height
        WIDTH = self.__width
        img = self.__data
        side = self.__side

        point1 = (HEIGHT - side)//2 - 1
        point2 = HEIGHT - (HEIGHT - side)//2
        point3 = (WIDTH - side)//2 - 1
        point4 = WIDTH - (WIDTH - side)//2

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if i <= point1 or i >= point2 or j <= point3 or j >= point4:
                    img[i][j] = (0,0,0)

    def toImage(self, data, mode):
        self.__grayData = data
        self.__grayImage = ImageTk.PhotoImage(Image.fromarray(data,mode=mode))
        return self.__grayImage

    def image(self):

        if self.__image == None:
            self.__image = ImageTk.PhotoImage(Image.fromarray(self.__data,mode="RGB"))
        
        return self.__image

    def focus(self):

        HEIGHT = self.__height
        WIDTH = self.__width
        img = self.__data
        side = self.__side

        point1 = (HEIGHT - side)//2 - 1
        point2 = HEIGHT - (HEIGHT - side)//2
        point3 = (WIDTH - side)//2 - 1
        point4 = WIDTH - (WIDTH - side)//2

        data = []

        for i in range(HEIGHT):
            if i <= point1 or i >= point2:
                continue

            row = []
            for j in range(WIDTH):
                if j <= point3 or j >= point4:
                    continue

                row.append(img[i][j])
            data.append(row)
        
        return data

    def focus2(self):

        HEIGHT = self.__height
        WIDTH = self.__width
        img = self.__grayData
        side = self.__side

        point1 = (HEIGHT - side)//2 - 1
        point2 = HEIGHT - (HEIGHT - side)//2
        point3 = (WIDTH - side)//2 - 1
        point4 = WIDTH - (WIDTH - side)//2

        data = []

        for i in range(HEIGHT):
            if i <= point1 or i >= point2:
                continue

            row = []
            for j in range(WIDTH):
                if j <= point3 or j >= point4:
                    continue

                row.append(img[i][j])
            data.append(row)
        
        return data

