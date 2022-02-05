from tkinter import *
import time 


def btn_clicked():
    print("Button Clicked")


window = Tk()


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

background_img = PhotoImage(file = "assets/background.png")
background = canvas.create_image(
    500.0, 267.5,
    image=background_img)




window.resizable(False, False)
window.mainloop()
