import tkinter as tk
from tkinter.constants import INSERT

from cv2 import buildOpticalFlowPyramid
from Bia import *
import random
import json
from matplotlib import pyplot as plt

def save_image(database, data, label):

    database.append((data, int(label)))


def read_database(url):

    # the size are 300x300 and each pixel in range [0,255]
    print("aaa")
    db = []

    WIDTH = 300
    HEIGHT = 300

    # db = [image, label]

    file = open(url, "rb")
    byte = file.read(1)

    x = 0
    y = 0
    row = []
    image_data = []

    while byte:
        row.append(int.from_bytes(byte, byteorder="big", signed=False))
        x = x + 1

        if x == WIDTH:
            image_data.append(row)
            y = y + 1
            x = 0
        
        if y == HEIGHT:
            byte = file.read(1)
            label = int.from_bytes(byte, byteorder="big", signed=False)
            y = 0
            db.append((image_data, label))

        byte = file.read(1)
    
    file.close()
    return db

def save_database(url, database):

    file = open(url, "wb")

    size = len(database)

    for i in range(size):

        for x in range(300):
            for y in range(300):
                pixel = int(database[i][0][x][y])
                byte = pixel.to_bytes(length=1, byteorder='big')
                file.write(byte)
        
        label = int(database[i][1])
        byte = label.to_bytes(length=1, byteorder='big')
        file.write(byte)
    
    file.close()

def render(page: Page):

    # get the image database
    database = read_database("database/byte_images.bin")

    FPS = 3

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
    timer = Timer(1/FPS, handle.timer)
    

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
                if state == 0:
                    code = False
                    alive = False
                elif state == 1:
                    text1_content.set("Faça o seguinte símbolo")
                    state = 0
            
            elif event["name"] == "confirm":
                if state == 0:
                    img = camera.getPhoto()
                    img.paint()
                    gray_img = img.imageSegmentation()
                    text1_content.set("Deseja salvar a imagem?")
                    cam_label.config(image=img.toImage(gray_img,"L"))

                    state = 1
                else:
                    save_image(database, img.focus2(), text2_content.get())
                    text1_content.set("Faça o seguinte símbolo")
                    text2_content.set(str(random.randint(0,9)))

                    state = 0

    # extremaly important!!! Kill the timer and camera threads!!!
    timer.kill()
    camera.kill()

    # save the database

    save_database("database/byte_images.bin", database)

    return code