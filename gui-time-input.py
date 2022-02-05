"""Import Modules"""
from tkinter import *
import csv
# from PIL import ImageTk, Image
from tkinter import messagebox


"""Required Functions"""

def submit_active():
    time_interval_info_active = intro_active_entry.get()

    """updatedlist = []
    temporarylist = []

    with open("time.txt", newline="") as f:
        reader = list(csv.reader(f))  # convert iterable to a list to make it easier
        print("Changing active timings...")
        S_NO = 1
        temporarylist = reader  # store a copy of the data

        for row in reader:  # for every row in the file
            for field in row:
                if field == S_NO:  # if a field is == to the required username
                    updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
                    new_time_active = time_interval_info_active
                    updatedlist[0][1] = new_time_active  # set the field for password to the new password

        updatepassword(updatedlist, temporarylist)"""
    intro_active_entry.delete(0, END)


    messagebox.showinfo('Updated', 'Time Interval Updated!')


def submit_sleep():
    time_interval_info_sleep = intro_sleep_entry.get()

    """updatedlist = []
    temporarylist = []

    with open("time.txt", newline="") as f:
        reader = list(csv.reader(f))  # convert iterable to a list to make it easier
        print("Changing sleep timings...")
        S_NO = 1
        temporarylist = reader  # store a copy of the data

        for row in reader:  # for every row in the file
            for field in row:
                if field == S_NO:  # if a field is == to the required username
                    updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
                    new_time_sleep = time_interval_info_sleep
                    updatedlist[0][2] = new_time_sleep  # set the field for password to the new password

        updatepassword(updatedlist, temporarylist)"""
    intro_sleep_entry.delete(0, END)

    messagebox.showinfo('Updated', 'Time Interval Updated!')



"""def updatepassword(updatedlist, temporarylist):
    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist  # replace old record with updated records

    with open("time.txt", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(temporarylist)
        print("File has been updated")"""


def back_home():
    home.pack(fill='both', expand=1)
    active.pack_forget()
    sleep.pack_forget()


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


# Defining different frames

home = Frame(root)
active = Frame(root)
sleep = Frame(root)

# Headline
heading = Label(root, text="Time Settings", font=("Rockwell", 28), bg="#3477eb", width="300", height="3", fg="white")
heading.pack()

"""Buttons for changing options to edit, i.e. sleep or active time intervals"""
btn1 = Button(root, text="ACTIVE", command=change_active, height="1", font=("Rockwell", 15), bg="#3477eb", fg="white")
btn1.place(x=40, y=150)

btn2 = Button(root, text="SLEEP", command=change_sleep, height="1", font=("Rockwell", 15), bg="#3477eb", fg="white")
btn2.place(x=500, y=150)

"""Adding Input Boxes"""

# Sleep Frame

intro_sleep = Label(sleep, text="Interval for which you want the P.C. to sleep(sec):", fg='#3477eb',
                    font=("Bookman Old Style", 12, "bold"))
intro_sleep.place(x=50, y=130)
intro_sleep_entry = Entry(sleep, bd=3, fg="#3477eb", font=("Bookman Old Style", 13))
intro_sleep_entry.place(x=70, y=180)

# Submit Button
sub_btn = Button(sleep, text='SUBMIT', command=submit_sleep, border=3, font=("Rockwell", 10, "bold"))
sub_btn.place(x=70, y=230)


# Active Frame

intro_active = Label(active, text="Interval for which you want the P.C. to stay awake(min.):", fg='#3477eb',
                     font=("Bookman Old Style", 12, "bold"))
intro_active.place(x=50, y=130)
intro_active_entry = Entry(active, bd=3, fg="#3477eb", font=("Bookman Old Style", 13))
intro_active_entry.place(x=70, y=180)

# Submit Button
sub_btn = Button(active, text='SUBMIT', command=submit_active, border=3, font=("Rockwell", 10, "bold"))
sub_btn.place(x=70, y=230)


mainloop()
