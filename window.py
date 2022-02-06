"""improting modules"""
from tkinter import *
import time



"""defining basic prompt window structure"""
window = Tk()
window.title('Prompt Window')
window.iconbitmap('image/prompt_icon.ico')

"""showing out the structure
and the frontend part of the promt 
window"""
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

"""the background image prompt in
accordance with 20-20-20 rule"""
background_img = PhotoImage(file = "image/background.png")
background = canvas.create_image(
    500.0, 267.5,
    image=background_img)





window.resizable(False, False)
window.mainloop()
