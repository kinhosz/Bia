from Bia import *
from tkinter import Event


class HandleEvent():

    def __init__(self, buffer: Queue):
        self.buffer = buffer

    def button(self, name):
        event = {}
        event["origin"] = "button"
        event["name"] = name

        self.buffer.push(event)

    def timer(self):
        event = {}
        event["origin"] = "timer"

        self.buffer.push(event)

    def keyboard(self, data: Event):
        print("estou aqui caralho")
        event = {}
        event["origin"] = "keyboard"
        event["type"] = self.getEventType(data.type)
        event["keycode"] = data.keycode
        event["time"] = data.time
        event["widget"] = data.widget
        event["x"] = data.x # relative to widget
        event["y"] = data.y
        event["x_root"] = data.x_root # relative to screen
        event["y_root"] = data.y_root

        self.buffer.push(event)

    def getEventType(self, type):

        if type == 36:
            return "Activate"	#A widget is changing from being inactive to being active. This refers to changes in the state option of a widget such as a button changing from inactive (grayed out) to active.
        elif type == 4:
            return "Button"	#The user pressed one of the mouse buttons. The detail part specifies which button. For mouse wheel support under Linux, use Button-4 (scroll up) and Button-5 (scroll down). Under Linux, your handler for mouse wheel bindings will distinguish between scroll-up and scroll-down by examining the .num field of the Event instance; see Section 54.6, “Writing your handler: The Event class”.
        elif type == 5:
            return "ButtonRelease"	#The user let up on a mouse button. This is probably a better choice in most cases than the Button event, because if the user accidentally presses the button, they can move the mouse off the widget to avoid setting off the event.
        elif type == 22:
            return "Configure"	#The user changed the size of a widget, for example by dragging a corner or side of the window.
        elif type == 37:
            return "Deactivate"	#A widget is changing from being active to being inactive. This refers to changes in the state option of a widget such as a radiobutton changing from active to inactive (grayed out).
        elif type == 17:
            return "Destroy"	#A widget is being destroyed.
        elif type == 7:
            return "Enter"	#The user moved the mouse pointer into a visible part of a widget. (This is different than the enter key, which is a KeyPress event for a key whose name is actually 'return'.)
        elif type == 12:
            return "Expose"	#This event occurs whenever at least some part of your application or widget becomes visible after having been covered up by another window.
        elif type == 9:
            return "FocusIn"	#A widget got the input focus (see Section 53, “Focus: routing keyboard input” for a general introduction to input focus.) This can happen either in response to a user event (like using the tab key to move focus between widgets) or programmatically (for example, your program calls the .focus_set() on a widget).
        elif type == 10:
            return "FocusOut"	#The input focus was moved out of a widget. As with FocusIn, the user can cause this event, or your program can cause it.
        elif type == 2:
            return "KeyPress"	#The user pressed a key on the keyboard. The detail part specifies which key. This keyword may be abbreviated Key.
        elif type == 3:
            return "KeyRelease"	#The user let up on a key.
        elif type == 8:
            return "Leave"	#The user moved the mouse pointer out of a widget.
        elif type == 19:
            return "Map"	#A widget is being mapped, that is, made visible in the application. This will happen, for example, when you call the widget's .grid() method.
        elif type == 6:
            return "Motion"	#The user moved the mouse pointer entirely within a widget.
        elif type == 38:
            return "MouseWheel"	#The user moved the mouse wheel up or down. At present, this binding works on Windows and MacOS, but not under Linux. For Windows and MacOS, see the discussion of the .delta field of the Event instance in Section 54.6, “Writing your handler: The Event class”. For Linux, see the note above under Button.
        elif type == 18:
            return "Unmap"	#A widget is being unmapped and is no longer visible. This happens, for example, when you use the widget's .grid_remove() method.
        elif type == 15:
            return "Visibility" #Happens when at least some part of the application window becomes visible on the screen.

        return -1 # not listed above
