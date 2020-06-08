from pynput import mouse
from pynput.mouse import Button, Controller
from os import system, name
#import os


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

mouse = Controller()
n = 1
while n == 1:
    # Read pointer position
    print('The current pointer position is {0}'.format(
        mouse.position))
    clear()
