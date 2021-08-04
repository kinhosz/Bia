import tkinter as tk
import time

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.__routes = {}
        self.__width = 600
        self.__height = 800
        self.__route = "homepage"
        self.__FPS = 30

        # inital configs
        self.__resize()

    def __resize(self):
        self.geometry(str(self.__height) + "x" + str(self.__width))
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
        while alive:
            print(self.__route)
            page = self.__getPage()
            alive = page.render()

        
