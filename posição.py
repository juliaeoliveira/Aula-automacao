import pyautogui
import time
pyautogui.PAUSE = 0.5
#espera um tempo para rodar
time.sleep(5)

#pegar posição do mouse
print(pyautogui.position())

#rolar a página - número negativo = scroll para baixo
#pyautogui.scroll(-1550)

#mostrar todas as teclas
#print(pyautogui.KEYBOARD_KEYS)

