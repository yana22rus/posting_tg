#!/usr/bin/env python3

from random import randint
from time import sleep
import pyautogui
import os



os.system("/usr/bin/telegram-desktop &")

sleep(4)

img = pyautogui.locateOnScreen("img.png")

sleep(1)

pyautogui.click(img)

sleep(2)

for x in range(1,10):

    pyautogui.moveTo(604,1050)

    pyautogui.click()

    sleep(1)

    pyautogui.hotkey("ctrl","l")

    sleep(1)

    path = "aaa"#хардкод

    count_file = len(os.listdir(path))

    pyautogui.write(f"{path}aaa{randint(1,count_file)}.gif")#хардкод

    sleep(1)

    pyautogui.hotkey("enter")

    sleep(1)

    pyautogui.hotkey("enter")

    sleep(10)

sleep(10)

pyautogui.hotkey("alt","f4")

