import pyautogui
import pyscreeze
import time
import keyboard
from PIL import Image

procura_imagem = 'sim'
move_x = 97
escreva = 'Python'


while procura_imagem == "sim":
    pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
    pyautogui.USE_IMAGE_NOT_FOUND_EXCEPTION = False

    try:
        img = pyautogui.locateCenterOnScreen('imagem/home.png', confidence=0.8)
        pyautogui.moveTo(img.x, img.y)
        time.sleep(3)
        campo = pyautogui.moveTo(img.x + move_x, img.y)
        time.sleep(1)
        pyautogui.click(img.x + move_x, img.y)
        pyautogui.write(escreva)
        keyboard.press_and_release('enter')
        procura_imagem = "não"
    except Exception as e:
        print(e)
        time.sleep(2)
        print('Imagem não visível')

pyautogui.alert('Finalizou!')