import pyautogui
import os
import time
var = 'tensorflow-gpu'  # change this name according to your anaconda environment name

location = os.getcwd()
pyautogui.press('win')
pyautogui.typewrite('anaconda prompt')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite('cd ' + location)
pyautogui.press('enter')
pyautogui.typewrite('conda activate ' + var)
pyautogui.press('enter')
pyautogui.typewrite('jupyter-notebook')
pyautogui.press('enter')