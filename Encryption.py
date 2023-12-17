# This program is to convert the message text to its morse code.

import tkinter as tk  # used for creating a GUI window
import DICT as DI  # Dictionary file is imported

encrypt = ''  # declaring encrypt as a global string


def encryption(string):  # function to convert the string to its morse code string
    cipher = ''
    Morse = DI.MORSE_CODE
    for letter in string:  # loop iteration till the end of the string
        if letter != ' ':
            cipher += Morse[letter] + ' '
        else:              # one space in mormal text is equal to two spaces in a morse code
            cipher += ' '
    return cipher


def call(message):
    global encrypt
    message = message.upper()  # string is converted to its upper case
    label['text'] = encryption(message)
    encrypt = label['text']

# below lines of code is used to create a window using tkinter module

root = tk.Tk()
root.title("Encryption")
canvas = tk.Canvas(root, height=500, width=600, bg='#17F8EF')
canvas.pack()

left_frame = tk.Frame(root, bg='#395A3F', bd=5)  # frame
left_frame.place(relx=0.05, rely=0.35, relwidth=0.35, relheight=0.4)

entry = tk.Entry(left_frame, font=40)            # entry
entry.place(relwidth=1, relheight=1)

button = tk.Button(root, text="GO!", font=40, command=lambda: call(entry.get()))    # button
button.place(relx=0.45, rely=0.5, relheight=0.1, relwidth=0.1)

right_frame = tk.Frame(root, bg='#BFD4BE', bd=5)  # frame
right_frame.place(relx=0.6, rely=0.35, relwidth=0.35, relheight=0.4)

label = tk.Label(right_frame, font=45, wraplength=100)  # label
label.place(relwidth=1, relheight=1)

root.mainloop()
