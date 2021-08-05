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

    frame = tk.Frame(parent, width=WIDTH, height=HEIGHT)
    frame.bind("<Key>", handle.keyboard)
    frame.grid()

    alive = parent.flip()

    canvas = tk.Canvas(frame, width=640, height=480)
    canvas.grid(column=0, row=0)

    head_text = "Faça o símbolo abaixo.\nPressione [espaço] para tirar uma foto"

    label = tk.Label(frame, text=head_text, font="ITALIC")
    label.grid(column=0, row=1)

    simbols = ["0","1","2","3","4","5","6","7","8","9"]

    pointer = 0

    simbol_label = tk.Label(frame, text="0", font="ITALIC")
    simbol_label.grid(column=1, row=1)

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
            if event["keycode"] == 32:
                pointer = (pointer + 1)%10
                simbol_label = tk.Label(frame, text=simbols[pointer], font="ITALIC")
                simbol_label.grid(column=1, row=1)

            else:
                print(event["keycode"])
    
    frame.destroy()
    t.kill()
    camera.kill()

    return False
    
