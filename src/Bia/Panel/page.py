class Page():

    def __init__(self, parent, render):
        self.__parent = parent
        self.__render = render

    def render(self):
        return self.__render(self)

    def parent(self):
        return self.__parent

    