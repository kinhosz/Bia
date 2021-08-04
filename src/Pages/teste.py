import tkinter as tk
from Bia import *
from datetime import datetime

def render(page: Page):

    FPS = 30

    buffer = Queue()
    handle = HandleEvent(buffer)

    t = Timer(1/FPS, handle.timer)
    t.start()

    parent = page.parent()
    frame = tk.Frame(parent)
    frame.bind("<Key>", handle.keyboard)
    frame.pack()

    canvas = tk.Canvas(frame,bg="pink", width=640, height=480)
    canvas.pack()

    camera = Vision()
    camera.start()

    frame.focus_set()

    alive = True

    parent.update()

    while alive:
        
        if buffer.empty():
            continue
        
        event = buffer.front()
        buffer.pop()
        if event["origin"] == "timer":
            imgT = camera.getPhoto()
            if imgT == None:
                continue

            imgT = camera.getPhoto()
            canvas.create_image((0,0),anchor=tk.NW, image=imgT)
            parent.update()

        elif event["origin"] == "keyboard":
            if event["keycode"] == 32:
                alive = False
            else:
                print(event["keycode"])

    
    frame.destroy()
    t.kill()
    camera.kill()

    return False
    
