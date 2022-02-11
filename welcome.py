# Imports
from tkinter import *
from gui_time import change_time


def welcome_screen(config):
    window = Tk()
    window.title('Welcome Window')
    window.iconbitmap('image/prompt_icon.ico')
    print(config["active"])
    window.state('zoomed')
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 2040,
        width = 2040,
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
        750.0, 250.0,
        image=background_img)
    active = config["active"]
    sleep = config["sleep"]
    canvas.create_text(
    750, 350,
    text = ("The current settings are"),
    fill = "#000000",
    font = ("Montserrat-Medium", int(48.0) ) )

    canvas.create_text(
    750, 450,
    text = (f"screen time: {active} minutes"),
    fill = "#000000",
    font = ("Montserrat-Medium", int(48.0) ) )
    canvas.create_text(
    750, 550,
    text = (f"break time: {sleep} seconds"),
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
        x = 875, y = 600,
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
        x = 170, y = 600,
        width = 463,
        height = 101)

    window.resizable(False, False)
    window.mainloop()
