import pyautogui
import time
import keyboard
import json
import random

input("press enter to continue")

list = open("list.json", "r")
list = json.load(list)

time.sleep(10)

while(True):
    pyautogui.write(i, interval=0.25)

def emoji_loop():
	while(True):
		for i in range(65):
			random.shuffle(list)
			pyautogui.write(list[i], interval=0.1)

emoji_loop()