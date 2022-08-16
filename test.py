# Import the tkinter library
from tkinter import *

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")


def open_win():
    top = Toplevel(win)
    top.geometry("700x250")
    Label(top, text="Hey Folks!", font=('Helvetica 14 bold')).pack()
    top.grab_set()


# Create a Label to print the Name
label = Label(win, text="Click the below Button to open the Popup", font=('Helvetica 18 bold'))
label.pack(pady=30)

# Create a Button
button = Button(win, text="Click Me", command=open_win, font=('Helvetica 14 bold'), foreground='OrangeRed3',
                background="white")
button.pack(pady=50)
win.mainloop()
