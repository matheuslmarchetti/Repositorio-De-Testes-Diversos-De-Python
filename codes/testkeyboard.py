import keyboard
import time
import pyautogui
import pyscreeze
from PIL import Image
import sys

continua = 'sim'
continua_de_novo = 'sim'
posicao = (0, 767)


pyautogui.useImageNotFoundException = False
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

try:
    while continua == 'sim':
        if pyautogui.locateOnScreen(fr'imagem\Captura de tela 2024-03-24 000808.png', confidence=0.8):
            print('saiu do loop')
            continua = 'não'
        elif keyboard.is_pressed('x'):
            pyautogui.alert('RPA PAUSE')
            continue
        else:
            print('imagem não visivel')
    time.sleep(3)
    while continua_de_novo == 'sim':
        if pyautogui.locateOnScreen(fr'imagem\Captura de tela 2024-03-24 000808.png', confidence=0.8):
            print('saiu do loop')
            continua_de_novo = 'não'
        elif keyboard.is_pressed('x'):
            pyautogui.alert('RPA PAUSE')
            continue
        else:
            time.sleep(3)
            pyautogui.click(1271, 117)
            time.sleep(3)
            pyautogui.click(35, 562)
except KeyboardInterrupt:
    pyautogui.alert('RPA PAUSE')