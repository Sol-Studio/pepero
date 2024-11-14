from pyautogui import position
from time import sleep
from os import system

while True:
    print(position())
    sleep(0.01)
    system("cls")
