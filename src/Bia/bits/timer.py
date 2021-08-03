import time
from threading import Thread

class Timer(Thread):

    def __init__(self, ms, task):
        Thread.__init__(self)
        self.__ms = ms
        self.__ALIVE = True
        self.__task = task
    
    def run(self):

        while self.__ALIVE:
            self.__task()
            time.sleep(self.__ms)
            

    def kill(self):
        self.__ALIVE = False
