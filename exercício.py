import pyautogui
import time
pyautogui.FAILSAFE= True
pyautogui.PAUSE = 0.5
time.sleep(3)

pyautogui.hotkey("ctrl", "t")

pyautogui.write("Youtube")

pyautogui.press("enter")


pyautogui.moveTo(x=252, y=358, duration= 1)

pyautogui.click(x=252, y=358, duration= 1 )

pyautogui.moveTo(x=715, y=166, duration= 1)

pyautogui.click(x=715, y=166, duration= 1 )

pyautogui.write("as aventuras de ladybug")

pyautogui.press("enter")

pyautogui.scroll(-600)

pyautogui.moveTo(x=706, y=693, duration= 1)

pyautogui.click(x=706, y=693, duration= 1 )