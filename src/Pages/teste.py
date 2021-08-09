import tkinter as tk
from Bia import *
from datetime import datetime

def render(page: Page):

    FPS = 30

    buffer = Queue()
    handle = HandleEvent(buffer)

    camera = Vision()
    camera.start()

    t = Timer(1/FPS, handle.timer)
    t.start()

    parent = page.parent()
    WIDTH, HEIGHT = parent.shape()
    Pallete = parent.getPallete()

    frame = tk.Frame(parent, width=WIDTH, height=HEIGHT, bg=Pallete["background"])
    frame.bind("<Key>", handle.keyboard)
    frame.grid()

    #area_1 = tk.Frame(frame, width=650, height=600)
    #area_1.pack(side="left", fill="both",expand="true")
    #area_2 = tk.Frame(frame,width=550, height=600,bg="red")
    #area_2.pack(fill="both", expand="true")

    canvas = tk.Canvas(frame, width=640, height=480)
    canvas.pack()

    #label = tk.Label(area_2, text="oi", background=Pallete["background"])
    #label.pack()

    frame.focus_set()

    alive = parent.flip()

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
            alive = parent.flip()

        elif event["origin"] == "keyboard":
            print(event["keycode"])
    
    frame.destroy()
    t.kill()
    camera.kill()

    return False
    
