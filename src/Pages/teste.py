import tkinter as tk
from Bia import *

def render(page: Page):

    buffer = Queue()
    handle = HandleEvent(buffer)

    t = Timer(1, handle.timer)
    t.start()

    parent = page.parent()
    frame = tk.Frame(parent)
    frame.bind("<Key>", handle.keyboard)
    frame.pack()

    frame.focus_set()

    while True:
        parent.update()
        if buffer.empty() == False:
            ev = buffer.front()
            buffer.pop()

            print(ev["origin"])
            if ev["origin"] == "keyboard" and ev["keycode"] == 32:
                break
    
    frame.destroy()
    t.kill()

    return False
    
