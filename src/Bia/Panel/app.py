import tkinter as tk
import time

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.__routes = {}
        print("If the screen is small please change the width to 1800 and height to 800 at file app.py")
        self.__width = 1200
        self.__height = 600
        self.__route = "homepage"
        self.__FPS = 15
        self.__close = False
        ### Pallete
        self.__pallete = {
            "background": "#3C3C3C",
            "confirm": "#378512",
            "cancel": "#9F0D09",
            "border": "#F3F1F1",
            "main": "#D85201",
            "meta": "#3E0427"
        }
        ### Text
        self.__text = {
            "font": "Lemon milk",
            "style": "bold",
            "h0": 100,
            "h1": 50,
            "h2": 30,
            "h3": 15,
            "h4": 10,
            "h5": 5
        }

        # inital configs
        self.__resize()
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

    def getText(self):
        return self.__text

    def getPallete(self):
        return self.__pallete

    def shape(self):
        return (self.__width, self.__height)

    def __on_close(self):
        self.__close = True

    def flip(self):
        if self.__close:
            return False
        
        self.update()
        return True

    def __resize(self):
        self.geometry(str(self.__width) + "x" + str(self.__height))
        self.resizable(False,False)

    def resize(self, widht, height):
        self.__width = widht
        self.__height = height
        self.__resize()

    def register(self, route, page):
        self.__routes[route] = page

    def setRoute(self, route):
        if route not in self.__routes.keys():
            self.__error(route + " dont exist")
            self.__route = "homepage"
        else:
            self.__route = route

    def __error(self, errorMsg):
        print(errorMsg)

    def __getPage(self):
        page = self.__routes[self.__route]
        return page

    def render(self):
        alive = True
        while alive and self.__close == False:
            print(self.__route)
            page = self.__getPage()
            alive = page.render()

        
