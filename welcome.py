from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.state('zoomed')
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

background_img = PhotoImage(file = "resources/background.png")
background = canvas.create_image(
    750.0, 320.0,
    image=background_img)

img0 = PhotoImage(file = "resources/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 875, y = 425,
    width = 463,
    height = 101)

img1 = PhotoImage(file = "resources/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 170, y = 425,
    width = 463,
    height = 101)

window.resizable(False, False)
window.mainloop()
