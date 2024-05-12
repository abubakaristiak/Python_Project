import pyautogui
import time

for count in range(0, 11):
    pyautogui.typewrite("Sorry :( "+str(count))
    time.sleep(3)
    pyautogui.press("enter")