"""Import Modules"""
from tkinter import *
import json
from tkinter import messagebox

"""Required Functions"""


def change_time(config):
    def submit_active():
        time_interval_info_active = float(intro_active_entry.get())

        with open("./config.json", "w") as jsonObj:
            # config = json.load(jsonObj)
            config["active"] = time_interval_info_active
            # print(config)
            print(json.dumps(config))
            jsonObj.seek(0)
            jsonObj.truncate()
            jsonObj.write(json.dumps(config))

        intro_active_entry.delete(0, END)

        messagebox.showinfo('Updated', 'Time Interval Updated!')

    def submit_sleep():
        time_interval_info_sleep = float(intro_sleep_entry.get())
        with open("./config.json", "r+") as jsonObj:
            # config = json.load(jsonObj)
            config["sleep"] = time_interval_info_sleep
            print(config)
            print(json.dumps(config))
            jsonObj.seek(0)
            jsonObj.truncate()
            jsonObj.write(json.dumps(config))

        intro_sleep_entry.delete(0, END)

        messagebox.showinfo('Updated', 'Time Interval Updated!')

    def change_active():
        active.pack(fill="both", expand=1)
        sleep.pack_forget()

    def change_sleep():
        sleep.pack(fill="both", expand=1)
        active.pack_forget()

    """Adding required settings for window size"""
    root = Tk()
    root.geometry("600x500")
    root.resizable(False, False)
    root.title("Edit Time Settings")
    root.iconbitmap('image\computer_icon.ico')

    def continue_ahead():
        root.destroy()
        print("The gui-time box is closed")
        return

    # Defining different frames

    Frame(root)
    active = Frame(root)
    sleep = Frame(root)

    # Headline
    heading = Label(root, text="Time Settings", font=("Rockwell", 28), bg="#02c021", width="300", height="3",
                    fg="white")
    heading.pack()

    """Buttons for changing options to edit, i.e. sleep or active time intervals"""
    btn1 = Button(root, text="ACTIVE", command=change_active, height="1", font=("Rockwell", 15), bg="#02c021",
                  fg="white")
    btn1.place(x=22, y=150)

    btn2 = Button(root, text="SLEEP", command=change_sleep, height="1", font=("Rockwell", 15), bg="#02c021", fg="white")
    btn2.place(x=500, y=150)

    """Adding Input Boxes"""

    # Sleep Frame

    intro_sleep = Label(sleep, text="Interval for which you want the P.C. to sleep(sec):", fg='#02c021',
                        font=("Bookman Old Style", 12, "bold"))
    intro_sleep.place(x=50, y=130)
    intro_sleep_entry = Entry(sleep, bd=3, fg="#02c021", font=("Bookman Old Style", 13))
    intro_sleep_entry.place(x=70, y=180)

    # Submit Button
    sub_btn = Button(sleep, text='SUBMIT', command=submit_sleep, border=3, font=("Rockwell", 10, "bold"))
    sub_btn.place(x=70, y=230)

    # Active Frame

    intro_active = Label(active, text="Interval for which you want the P.C. to stay awake(min.):", fg='#02c021',
                         font=("Bookman Old Style", 12, "bold"))
    intro_active.place(x=50, y=130)
    intro_active_entry = Entry(active, bd=3, fg="#02c021", font=("Bookman Old Style", 13))
    intro_active_entry.place(x=70, y=180)

    # Submit Button
    sub_btn = Button(active, text='SUBMIT', command=submit_active, border=3, font=("Rockwell", 10, "bold"))
    sub_btn.place(x=70, y=230)

    # Continue button to destroy window
    # Submit Button
    PhotoImage(file="image/img1.png")
    b0 = Button(root,
                text="CONTINUE",
                command=continue_ahead,
                height="1",
                font=("Rockwell", 15),
                bg="#02c021",
                fg="white")

    b0.place(x=230, y=150, )

    mainloop()
