from PIL import ImageTk, Image

class Picture():

    def __init__(self, data):
        self.__data = data
        self.__height = len(data)
        
        if self.__height == 0:
            self.__width = 0
        else:
            self.__width = len(data[0])

        self.__image = None
        self.__side = 300

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

