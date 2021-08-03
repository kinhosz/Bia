from threading import Lock
import warnings

class Node():

    def __init__(self, data):
        self.__next = None
        self.__data = data

    def get(self):
        return self.__data

    def getNext(self):
        return self.__next
    
    def setNext(self, next):
        self.__next = next

class Queue():

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def push(self, data):
        lock = Lock()
        lock.acquire()
        
        node = Node(data)
        if self.__size == 0:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.setNext(node)
            self.__tail = self.__tail.getNext()
        
        self.__size = self.__size + 1
        lock.release()

    def empty(self):
        return self.__size == 0
    
    def size(self):
        return self.__size
    
    def pop(self):
        lock = Lock()
        lock.acquire()
        if self.__size == 0:
            warnings.warn("Impossible pop the queue, because it's empty")
        else:
            self.__head = self.__head.getNext()
            self.__size = self.__size - 1
        lock.release()

    def front(self):
        ret = None
        lock = Lock()
        lock.acquire()
        if self.__size == 0:
            warnings.warn("Impossible get from queue, because it's empty")
        else:
            ret = self.__head.get()
        lock.release()
        
        return ret

    def wait(self):

        while self.empty():
            pass
        return self.front()
        