import cv2, time
from threading import Thread, Lock
import warnings
from PIL import Image, ImageTk

class Vision(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.__ALIVE = True
        self.__video = cv2.VideoCapture(0)
        self.__frame = []

    def __del__(self):
        self.__video.release()

    def run(self):
        while self.__ALIVE:
            ret, frame = self.__video.read()
            if ret == False:
                warnings.warn("An error occured during get the frame")
                frame = None
            self.__frame = frame

    def getPhoto(self):
        frame = self.__frame 

        if frame == []:
            return None

        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        return ImageTk.PhotoImage(Image.fromarray(frame,mode="RGB"))

    def getFrame(self):
        return self.__frame

    def kill(self):
        self.__ALIVE = False


class Vision2(Thread):
    
    def __init__(self, fps=20):
        Thread.__init__(self)
        self.__FPS = fps
        self.__video = cv2.VideoCapture(0)
        self.__ALIVE = True
        self.__Frame = None
        self.__lock = Lock()
    
    def run(self):

        while self.__ALIVE:
            ret, frame = self.__video.read()
            if ret:
                self.__setFrame(frame)
            time.sleep(1/self.__FPS)

        self.__video.release()
        cv2.destroyAllWindows()

    def kill(self):
        self.__ALIVE = False

    def __setFrame(self, frame):
        self.__lock.acquire()
        self.__Frame = frame
        self.__lock.release()

    def getFrame(self):
        self.__lock.acquire()
        frame = self.__Frame
        self.__lock.release()
        
        return frame