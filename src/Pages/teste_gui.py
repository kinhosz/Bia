import tkinter as tk
from tkinter.constants import INSERT
from Bia import *
import random
import json

import numpy as np
def save_image(database, data, label):

    if "size" not in database.keys():
        database["size"] = 0
    if "images" not in database.keys():
        database["images"] = []
    
    database["size"] = database["size"] + 1

    height = len(data)
    if height == 0:
        width = 0
    else:
        width = len(data[0])

    data_sz = np.array(data).tolist()

    database["images"].append({
        "width": width,
        "height": height,
        "type": "RGB",
        "label": label,
        "image": data_sz
    })

def timerasync(parent, camera, cam_label, state):
    return ""

        

def render(page: Page):

    # get the image database
    f = open("database/images.json","r")
    database = json.loads(f.read())
    f.close()

    FPS = 15

    new_db = {}

    # get the root window reference
    parent = page.parent()

    # get shape of the window
    WIDTH, HEIGHT = parent.shape()

    # get the pallete of the window
    pallete = parent.getPallete()

    # get the text config
    text_style = parent.getText()

    # create a buffer
    buffer = Queue()

    # init handle response
    handle = HandleEvent(buffer)

    # get the key events
    parent.bind("<Key>", handle.keyboard)

    # create a gui workspace
    canvas = tk.Canvas(parent, width=WIDTH, height=HEIGHT, bg=pallete["meta"])
    canvas.grid(columnspan=4, rowspan=3)

    # init the cam
    camera = Vision()
    camera.start()

    # create a timer
    timer = Timer(1/3, handle.timer)
    

    timer.start()

    # create a cam label
    img = camera.getPhoto()
    cam_label = tk.Label(image=img.image(), background=pallete["border"])
    cam_label.grid(column=0, row=0, columnspan=2, rowspan=3,padx=20, pady=20)

    # create the text1_content of the page
    text1_content = tk.StringVar()
    text1_label = tk.Label(textvariable=text1_content, bg=pallete["meta"])
    text1_label.grid(column=2, row=0, columnspan=2)
    text1_label.config(font=(text_style["font"], text_style["h2"], text_style["style"]))
    text1_label.config(fg=pallete["border"])
    text1_content.set("Faça o seguinte símbolo")

    # create the text2_content of the page
    text2_frame = tk.Frame(parent, bg=pallete["background"],width=250, height=250)
    text2_frame.config(highlightbackground=pallete["border"], highlightthickness=2)
    text2_frame.grid(column=2, row=1, columnspan=2)
    text2_content = tk.StringVar()
    text2_label = tk.Label(textvariable=text2_content, bg=pallete["background"])
    text2_label.grid(column=2, row=1, columnspan=2)
    text2_label.config(font=(text_style["font"], text_style["h0"], text_style["style"]))
    text2_label.config(fg=pallete["main"])
    text2_content.set(str(random.randint(0,9)))

    # cancel button
    cancel_btn = tk.Button(text="Cancel [esc]", width=15, fg=pallete["border"])
    cancel_btn.config(bg=pallete["cancel"], command=lambda: handle.button("cancel"))
    cancel_btn.config(font=(text_style["font"], text_style["h3"], text_style["style"]))
    cancel_btn.grid(column=2, row=2)

    # confirm button
    confirm_btn = tk.Button(text="Confirm [space]", width=15, fg=pallete["border"])
    confirm_btn.config(bg=pallete["confirm"], command=lambda: handle.button("confirm"))
    confirm_btn.config(font=(text_style["font"], text_style["h3"], text_style["style"]))
    confirm_btn.grid(column=3, row=2)

    # create a boolean to available if the window is closed
    alive = parent.flip()

    # code to parent
    code = True

    # page state
    state = 0
    while parent.flip() and alive:

        if buffer.empty():
            continue
        print(buffer.front())
        
        event = buffer.front()
        
        buffer.pop()
        if event["origin"] == "timer":
            # t = Thread(target=timerasync, args=(parent, camera, cam_label, state,))
            # t.start()
            if state == 0:
                img = camera.getPhoto()

                img.drawSquare()
                cam_label.config(image=img.image())

        elif event["origin"] == "button":

            if event["name"] == "cancel":
                print("cancelou")
                if state == 0:
                    code = False
                    alive = False
                elif state == 1:
                    text1_content.set("Faça o seguinte símbolo")
                    state = 0
            
            elif event["name"] == "confirm":
                print("aqui porra")
                if state == 0:
                    img = camera.getPhoto()
                    img.paint()
                    
                    text1_content.set("Deseja salvar a imagem?")
                    cam_label.config(image=img.image())

                    state = 1
                else:
                    save_image(new_db, img.focus(), text2_content.get())
                    text1_content.set("Faça o seguinte símbolo")
                    text2_content.set(str(random.randint(0,9)))

                    state = 0

    # extremaly important!!! Kill the timer and camera threads!!!
    timer.kill()
    camera.kill()

    # save the database

    # easy to merge pull requests
    id = ""
    for i in range(30):
        id = id + str(random.randint(0,9))

    database[id] = new_db

    f = open("database/images.json","w")
    f.write(json.dumps(database))
    f.close()

    return code
    
