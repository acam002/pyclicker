
import os
from pynput import keyboard
from pynput.mouse import Button, Controller
#from pynput.keyboard import Listener
import random
from time import sleep
import sys

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


# Hi Luis, the two numbers below (10, 20) are x and y respectively, use clickLocation.py to find the numbers you want to start at.
n = 1
mouse = Controller()
mouse.position = (10, 20)
while n == 1:
    #random numbers being set within the ranges specified
    x = random.uniform(83, 87)
    y = random.uniform(90, 94)

    print(x)
    print(y)
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    
    sleep(random.uniform(1, 2)) # Time in seconds from 1 to 2
    
    x = random.uniform(83, 87)
    y = random.uniform(39, 41)
    print(x)
    print(y)
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    
    sleep(random.uniform(1, 2)) # Time in seconds from 1 to 2
    
    if listener.running == False:
        sys.exit(0)
    
