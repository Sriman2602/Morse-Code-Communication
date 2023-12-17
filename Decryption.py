# Program to convert the morse code received from detection to the text message

import tkinter as tk
import detection as de   # detection file is imported
import DICT as DI        # DICT file is imported


def decrypt(message):
    i = 0
    morse = DI.MORSE_CODE
    decipher = ''
    text = ''
    for letter in message:
        if letter != ' ':  # checks for the occurrence of only dots and dashes
            i = 0
            text += letter  # text gathers dots and dashes from the message until space
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morse.keys())[list(morse.values()).index(text)]
            # compares each values in the DICT with text if matches then its respected key is added to decipher
                text = '' # clears text
    return decipher

def call():
    mo_message = de.de_message
    label['text'] = decrypt(mo_message)


root = tk.Toplevel()      # creates another tkinter window Toplevel
root.title('Decryption')  # of name Decryption
canvas = tk.Canvas(root, height=500, width=600, bg='#738BFB')  # canvas
canvas.pack()

left_frame = tk.Frame(root, bg='#395A3F', bd=5)                # left_frame
left_frame.place(relx=0.05, rely=0.35, relwidth=0.35, relheight=0.4)

label = tk.Label(left_frame, font=40, text=str(de.de_message))  # label
label.place(relwidth=1, relheight=1)

button = tk.Button(root, text="GO!", font=40, command=lambda: call())  # button
button.place(relx=0.45, rely=0.5, relheight=0.1, relwidth=0.1)

right_frame = tk.Frame(root, bg='#BFD4BE', bd=5)                # right_frame
right_frame.place(relx=0.6, rely=0.35, relwidth=0.35, relheight=0.4)

label = tk.Label(right_frame, font=45, wraplength=100)          # label
label.place(relwidth=1, relheight=1)

root.mainloop()
