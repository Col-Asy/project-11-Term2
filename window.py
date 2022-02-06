"""improting modules"""
from tkinter import *
import time


"""defining basic prompt window structure"""
window = Tk()
window.title('Prompt Window')
window.iconbitmap('image/prompt_icon.ico')

"""showing out the structure and the 
frontend part of the promt window"""
window.state('zoomed')  #state is zoomed
window.configure(bg = "#ffffff")

"""making of the white background canvas"""
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1400,
    width = 1400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)  #the canvas is at (0,0)

"""defining a new function i.e when the button is 
clicked it'll end the sessionand close the window"""
def end_session():
    window.destroy()    #closes the window
    print("Session ended")

"""the background image prompt in
accordasnce with 20-20-20 rule"""
background_img = PhotoImage(file = "image/background.png")
background = canvas.create_image(
    750.0, 320,     #(x,y)
    image=background_img)

"""attributes of button"""
img0 = PhotoImage(file = "image/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = end_session,
    relief = "flat")

"""defining the co-ordinates of the button"""
b0.place(
    x = 526, y = 425,
    width = 463,
    height = 101)


window.resizable(False, False)
window.mainloop()