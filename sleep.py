"""Importing tkinter and time module"""
from tkinter import *
import time 




"""defining sleep screen"""
root = Tk()
root.title('Sleep Screen')
root.iconbitmap('image/prompt_icon.ico')


"""setting the background for screen 
as black and zoomed out for full mode"""
root.config(bg="black")
root.state('zoomed')

"""after a certain duration 
the screen will withdraw"""
time.sleep(5)
root.withdraw()

root.mainloop()