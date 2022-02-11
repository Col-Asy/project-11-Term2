# Imports
from tkinter import *
from gui_time import change_time


def welcome_screen(config):
    window = Tk()
    print(config["active"])
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
    
    def settings():
        window.destroy()
        change_time(config)
        print("Settings is clicked")
    def continue_wel():
        window.destroy()
        print("The welcome window is now closed")
    #The current settings are (variable)

    background_img = PhotoImage(file = "image/welcome.png")
    background = canvas.create_image(
        750.0, 320.0,
        image=background_img)
    active = config["active"]
    sleep = config["sleep"]
    canvas.create_text(
    600, 500,
    text = (f"The current settings are screen time: {active} and break time: {sleep}"),
    fill = "#000000",
    font = ("Montserrat-Medium", int(48.0) ) )

    
    img0 = PhotoImage(file = "image/continue.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = continue_wel,
        relief = "flat")

    b0.place(
        x = 875, y = 685,
        width = 463,
        height = 101)

    img1 = PhotoImage(file = "image/settings.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = settings,
        relief = "flat")

    b1.place(
        x = 170, y = 685,
        width = 463,
        height = 101)

    window.resizable(False, False)
    window.mainloop()
