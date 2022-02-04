from tkinter import *
import time 


def btn_clicked():
    print("Button Clicked")


window = Tk()

def window_prompt(pop_up):
    

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 267.5,
    image=background_img)

if __name__ = '__main__':
    while True:



window.resizable(False, False)
window.mainloop()
