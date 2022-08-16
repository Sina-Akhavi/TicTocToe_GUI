import tkinter.messagebox as message
from tkinter import *
import backend
from backend import game

window = Tk()
window.geometry('400x500')
window.title("Tic Toc Toe")
window.resizable(width=False, height=False)

photo_x = PhotoImage(file=r".\XX.PNG")
photo_o = PhotoImage(file=r".\O.PNG")
photo_default = PhotoImage(file=r".\default.PNG")

counter = IntVar(window)
counter.set(1)

# ---------------------- Buttons ----------------------
button_1 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_1, 1, 1))
button_1.place(x=10, y=5)

button_2 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_2, 1, 2))
button_2.place(x=140, y=5)

button_3 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_3, 1, 3))
button_3.place(x=275, y=5)

button_4 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_4, 2, 1))
button_4.place(x=10, y=130)

button_5 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_5, 2, 2))
button_5.place(x=140, y=130)

button_6 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_6, 2, 3))
button_6.place(x=275, y=130)

button_7 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_7, 3, 1))
button_7.place(x=10, y=255)

button_8 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_8, 3, 2))
button_8.place(x=140, y=255)

button_9 = Button(window, image=photo_default, borderwidth=0, bg='yellow', command=lambda: set_image(button_9, 3, 3))
button_9.place(x=275, y=255)

text_exit = StringVar()
text_exit.set('EXIT')
exit_button = Button(window, textvariable=text_exit, font=('Times New Roman', 12, 'bold'), width=12, height=2,
                     bg='orange',command=window.destroy, fg='red')
exit_button.place(x=70, y=420)

text_start_again = StringVar()
text_start_again.set('Start Again')
start_again_button = Button(window, textvariable=text_start_again,
                            font=('Times New Roman', 12, 'bold'), width=12, height=2, bg='orange',
                            command=lambda: clear(), fg='red')

start_again_button.place(y=420, x=210)


# ---------------------- win_windows ----------------------
def show_result(result):
    win_window = Toplevel(window)
    win_window.title('game ended')
    win_window.geometry('300x100')

    label = Label(win_window, text=result, borderwidth=0, width=22,
                  font=('Helvetica', 18, 'bold', 'italic'), fg='red')
    start_again = Button(win_window, text='New Game', width=10, height=2, bg='orange',
                         font=('Times New Roman', 10, 'bold'), command=lambda: clear(win_window))
    start_again.place(x=105, y=50)
    label.pack()
    win_window.grab_set()


# ---------------------- commands ----------------------
def handle_turn(button, row, column, player_letter):
    game.perform_player_choice(row, column, player_letter)

    if player_letter == 'o':
        button.configure(image=photo_o)
    else:
        button.configure(image=photo_x)

    counter.set(counter.get() + 1)


def set_image(button, row, column):
    if not game.is_allowed_to_choose(row, column):
        message.showerror("Error", "You cannot choose this button!!!")
        return

    if is_o_turn():
        handle_turn(button, row, column, 'o')
        if game.is_won():
            show_result('O Won!!!')
            return
    else:
        handle_turn(button, row, column, 'x')
        if game.is_won():
            show_result('X Won!!!')
            return

    if counter.get() == 10:
        show_result('Draw!!!')


def clear(win_window=None):
    button_1.configure(image=photo_default)
    button_2.configure(image=photo_default)
    button_3.configure(image=photo_default)
    button_4.configure(image=photo_default)
    button_5.configure(image=photo_default)
    button_6.configure(image=photo_default)
    button_7.configure(image=photo_default)
    button_8.configure(image=photo_default)
    button_9.configure(image=photo_default)

    backend.game.clear()
    counter.set(1)
    if win_window is not None:
        win_window.destroy()


def is_o_turn():
    return counter.get() % 2 == 0


window.mainloop()
