import keyboard
import pyautogui
import time

time.sleep(3)
pyautogui.click(994, 286)
time.sleep(1)
keyboard.press('home')
time.sleep(1)
# keyboard.send('shift+end')
pyautogui.hotkey('ctrl','shiftright','shiftleft','end')