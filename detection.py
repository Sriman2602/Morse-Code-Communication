import LIGHT
import time

print("DETECTION PROGRAM")
morse = LIGHT.l_message  # morse now contains the message from the flash signal
print(morse)
i = 0
de_message = ""
time.sleep(2)
print("\nMESSAGE DETECTED")
time.sleep(0.5)
print("DECODING...")
while i < len(morse):  # loop iteration until end of the morse
    time.sleep(0.4)    # delay of 0.4 seconds
    if morse[i] == "ON":  # checks if the current element is 'ON'
        if morse[i+1] == "OFF":  # checks if the next element is 'OFF'
            de_message += '.'  # adds a dot to de_message
            print(morse[i], morse[i+1], end="\t\t\t")
            print(".")
            i += 1
        elif morse[i+1] == morse[i+2] == "ON" and morse[i+3] == "OFF":
            de_message += '-'  # adds dash to the de_message
            print(morse[i], morse[i + 1], morse[i+2], morse[i+3], end="\t")
            print("-")
            i += 3
    else:
        if morse[i+1] == morse[i+2] == "OFF":
            de_message += " " # adds space to the de_message
            print(morse[i], morse[i + 1], morse[i+2], end="\t\t\t")
            i += 2
            print(" ")
    i += 1
print("\nMORSE CODE:", de_message)
