import keyboard
import pyautogui
import time
from win32api import GetKeyState
from win32con import VK_NUMLOCK


time.sleep(3)
if GetKeyState(VK_NUMLOCK) == 1:
    print ("NUM LOCK is on.")
    keyboard.press_and_release('numlock')
    time.sleep(1)
    pyautogui.click(432, 248)
    time.sleep(1)
    keyboard.press_and_release('home')
    time.sleep(1)
    keyboard.press_and_release('shift+end')
elif GetKeyState(VK_NUMLOCK) == 0:
    print ("NUM LOCK is off.")
    time.sleep(1)
    pyautogui.click(432, 248)
    time.sleep(1)
    keyboard.press_and_release('home')
    time.sleep(1)
    keyboard.press_and_release('shift+end')


# if GetKeyState(VK_NUMLOCK) == 1:
#     print ("NUM LOCK is on.")
#     time.sleep(1)
#     pyautogui.click(432, 248)
#     time.sleep(1)
#     keyboard.press_and_release('home')
#     time.sleep(1)
#     #seleciona linhas abaixo dependendo do sistema
#     pyautogui.hotkey('ctrl','shiftright','shiftleft','end')
# elif GetKeyState(VK_NUMLOCK) == 0:
#     print ("NUM LOCK is off.")

# time.sleep(3)
# pyautogui.click(432, 248)
# time.sleep(1)
# keyboard.press('home')
# keyboard.press_and_release('home')
# time.sleep(1)
# keyboard.send('shift+end')
# keyboard.press_and_release('shift+end')
# pyautogui.hotkey('ctrl','shiftright','shiftleft','end')