import tkinter #inbuilt package
import cv2 #computer vision library #pip install opencv-python
import PIL.Image, PIL.ImageTk #pip install pillow #PIL is the Python Imaging Library
from functools import partial # in order to run command name of defined functions with parameters ex: def play(dsdss), in this dsdss is the thing we can run using functools, but it was not possible without that
import threading
import imutils
import time
def play(speed):
    print(f"your speed is {speed}")

def pending(decision):

# STEPS
    # 1. display decision pending image
frame = cv2.cvtColor(cv2.imread(pending.png), cv2.COLOR_BGR2RGB)
frame = imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
frame = PIL.ImageTk.PhotoImage(image=frame,anchor=tkinter.NW)
canvas.image = frame
canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. wait for 1 second
    # 3. display sponsor image
    # 4. wait for 1.5 second
    # 5. display decision : out/not out image
    # 6. wait for 1.5 second



def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start
    print("the player is out")

def notout():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon=1
    thread.start
    print("the player is not out")


SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()       #took window as a variable for uing tkinter
window.title("DRS SYSTEM USING PYTHON") #gave the title


#canvas = The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.
# w = Canvas ( master, option=value, ... ) #syntax <----
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image=photo)
canvas.pack()


#buttons to put in the window 

btn = tkinter.Button(window, text = "<<<previous(fast)", width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<<<previous(slow)", width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = "next(slow)>>>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text= "next(fast)>>>", width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = "give not out", width = 50) 
btn.pack()

btn = tkinter.Button(window, text = "give out", width = 50)
btn.pack()



window.mainloop() #used to run the main program and events in the tkinter 


