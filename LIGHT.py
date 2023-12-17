# The timing in Morse code is based around the length of one dot (“.”).
# From the dit length we can derive the length of a dash (“-”) and the various pauses
# Dot: 1 unit
# Dash: 3 units
# Intra-character space (the gap between dots and dash within a character): 1 unit
# Inter-character space (the gap between the characters of a word): 3 units
# Word space (the gap between two words): 6 units


import Encryption as En  # importing Encryption file
import turtle
import time

message = En.encrypt
print("Message to be transmitted: ", message)
wn = turtle.Screen()  # creates a virtual screen
wn.title("MESSAGE")   # named MESSAGE
wn.bgpic("Background.png")  # adding background image
l_message = list()  # list to add the status of the signal after 1 unit of delay

# FLASH LIGHT
flash_light = turtle.Turtle()  # calling turtle pointer
flash_light.shape("circle")    # in circular shape
flash_light.color("yellow")     # and black in colour


# TIME
time.sleep(1)
print("TRANSMITTING...")
for i in range(0, len(message)):  # loop
    print(message[i], end='')
    time.sleep(0.25)              # delay of 0.25 seconds
    if message[i] == ".":
        flash_light.color("yellow")  # changes turtle colour to yellow
        l_message.append("ON")
        time.sleep(0.5)              # delay of 1 unit
        flash_light.color("black")   # changes turtle colour to black
    elif message[i] == "-":
        flash_light.color("yellow")
        for _ in range(3):
            time.sleep(0.5)
            l_message.append("ON")
        flash_light.color("black")
    else:
        for _ in range(2):
            time.sleep(0.5)
            l_message.append("OFF")
    time.sleep(0.25)
    l_message.append("OFF")
print("\nMESSAGE TRANSMITTED SUCCESSFULLY")
