"""improting modules"""
import imp
from tkinter import *

"""Defining a new variable screen_break that 
pops up the break screen as per the active and
sleep time"""


def screen_break(brTime):
    window = Tk()
    window.title('Prompt Window')
    window.iconbitmap('image/prompt_icon.ico')
    """showing out the structure and the 
    frontend part of the promt window"""
    window.state('zoomed')  # state is zoomed
    window.configure(bg="#ffffff")

    """making of the white background canvas"""
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=1400,
        width=1400,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)  # the canvas is at (0,0)

    """defining a new function i.e when the button is 
    clicked it'll initialize the skip break"""

    def end_session():
        window.destroy()  # closes the window
        print("Break skipped")

    """the background image prompt in
    accordasnce with 20-20-20 rule"""
    background_img = PhotoImage(file="image/background.png")
    canvas.create_image(
        750.0, 320,  # (x,y)
        image=background_img)

    """attributes of button 2"""
    img0 = PhotoImage(file="image/img1.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=end_session,
        relief="flat")

    """defining the co-ordinates of the button"""
    b0.place(
        x=875, y=425,
        width=463,
        height=101)

    """"The function to compeletely terminate 
    the programme"""

    def end_script():
        print("The code is ended")
        exit()

    """attributes of the Button 2"""
    img1 = PhotoImage(file="image/img0.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=end_script,
        relief="flat")

    b1.place(
        x=170, y=425,
        width=463,
        height=101)

    copyright = PhotoImage(file="image/copy.png")
    canvas.create_image(
        780.0, 820,  # (x,y)
        image=copyright)

    window.resizable(False, False)
    window.after(brTime * 1000, lambda: window.destroy())  # After the scheduled time window.destroy()
    window.mainloop()
