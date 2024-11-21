# Automação com pyautogui
#Automatizar tarefas repititivas ou um processo no sistema ERP 
import pyautogui 
import time
#Para não perder controle da sua automação
pyautogui.FAILSAFE= True

#Pausa geral de 0.3 seg (300 milissegundos)
pyautogui.PAUSE = 0.3

#espera um tempo para rodar
time.sleep(5)

#pegar posição do mouse
#print(pyautogui.position())

#pegar resolução de tela
#print(pyautogui.size())

#clicar com mouse
pyautogui.click(x= 355, y= 395)

#clicar com botão direito do mouse
#pyautogui.click(x= 355, y= 395, button= "right")

# Dois clicks no mouse
#pyautogui.click(x= 355, y= 395, clicks= "2")

#mover o mouse
pyautogui.moveTo(x=683, y=231, duration= 1)

#pyautogui.moveTo(x=849, y=271, duration= 2)

pyautogui.click(x=1179, y=310)

pyautogui.scroll(-1650)

pyautogui.click(x=977, y=740, duration= 1 )

#Funções do teclado
pyautogui.press("win")

#Para escrever 
pyautogui.write("Clima", intervalo= 0.25)

pyautogui.press("enter")

#Para pressionar duas teclas ao mesmo tempo
pyautogui.hotkey("ctrl, v")