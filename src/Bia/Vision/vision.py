import cv2, time
from threading import Thread, Lock

class Vision():
    
    def __init__(self):
        self.__video = cv2.VideoCapture(0)

    def __del__(self):
        self.__video.release()

    def getFrame(self):
        ret, frame = self.__video.read()
        if ret == False:
            print("errorrrr")
        return frame


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