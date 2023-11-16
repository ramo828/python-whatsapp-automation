# pip install pywhatkit
import pywhatkit as kit
from extensions import keyboard
from time import sleep
import os
from random import randint

message = "Hello from Python! This is an instant WhatsApp message."
numbers= ""
image = False

def send_image():
    kit.sendwhats_image(number, "images/img.jpg")
    sleep(10)
    keyboard.new_tab()
    sleep(5)
    keyboard.write(os.getcwd()+"/images/img.jpg")
    sleep(3)
    keyboard.enter()
    sleep(2)
    keyboard.mouseKey(1)
    sleep(3)
    for _ in range(3):
        keyboard.down()
    keyboard.enter()
    sleep(2)
    keyboard.close_tab()
    sleep(3)
    keyboard.paste()
    sleep(3)
    keyboard.enter()
    sleep(3)
    keyboard.close_tab()

with open("numbers.txt", "r") as numb:
    numbers = numb.read()

# Specify the phone number (with country code) and the message
with open(f"message/{randint(0,2)}", "r") as msg:
    message = msg.read()


for number in numbers.split("\n"):
    # Send the message instantly
    if(image):
        send_image()
    else:
        kit.sendwhatmsg_instantly(number, message)
        sleep(10)
        keyboard.enter()
        sleep(3)
        keyboard.close_tab()
   