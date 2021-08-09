import tkinter as tk
from tkinter import ttk
import time
from Bia import *

def handle(L):
    print("cliquei caralho")
    L.append("click")

def sayHi():
    pass

def render(page: Page):

    L = []

    parent = page.parent()
    pallete = parent.getPallete()

    frame = tk.Frame(parent, bg=pallete["background"])
    frame.pack()

    cmd = tk.Button(frame, text="botao", command=lambda: handle(L))
    cmd.pack()

    t = Timer(1,sayHi)
    t.start()

    alive = True
    while alive:

        if len(L) > 0:
            alive = False
        parent.flip()

    frame.destroy()
    t.kill()
    parent.setRoute("teste")
    
    return True
