from tkinter import *
import keyboard
import mouse 
import time
win = Tk()
win.title('autoclicker')
win.geometry("400x400")
win.resizable(False, False)
win.mainloop()
Click = False
def clicker():
    global Click
    Click = not Click
keyboard.add_hotkey('W + S', clicker)
while True:
    if Click:
        mouse.click(button='left')
        time.sleep(0.01)
