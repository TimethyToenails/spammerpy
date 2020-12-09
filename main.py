import pyautogui
import time
import json
import random


list = open("list.json", "r")
list = json.load(list)

time.sleep(10)

def emoji_loop():
	while(True):
		for i in range(65):
			random.shuffle(list)
			pyautogui.write(list[i], interval=0.01)
		pyautogui.press('enter')

emoji_loop()