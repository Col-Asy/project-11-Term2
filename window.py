"""improting modules"""
from tkinter import *


def screen_break(brTime):
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
    
    def end_script():
        print("End of the loop")
        exit()
        
        

    img1 = PhotoImage(file = "image/img0.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = end_script,
        relief = "flat")

    b1.place(
        x = 400, y = 400,
        width = 463,
        height = 101)

    copyright = PhotoImage(file = "image/copy.png")
    background = canvas.create_image(
        780.0, 820,     #(x,y)
        image=copyright)

    window.resizable(False, False)
    window.after(brTime*1000,lambda:window.destroy())
    window.mainloop()