import pyautogui
import os
import time
import sys
var = sys.argv[1] if len(sys.argv) > 1 else 'fused'
ide = input('1. VS Code \n 2. Jupyter notebook \n (Press Enter to select Jupyter notebook by default) \n')

location = os.getcwd()
pyautogui.press('win')
pyautogui.typewrite('anaconda prompt')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite('cd ' + location)
pyautogui.press('enter')
if len(var) == 0:
    pyautogui.typewrite('conda activate fused')
else:
    pyautogui.typewrite('conda activate ' + var)
pyautogui.press('enter')
if ide == '1':
    pyautogui.typewrite('code .')
else:
    pyautogui.typewrite('jupyter-notebook')
pyautogui.press('enter')