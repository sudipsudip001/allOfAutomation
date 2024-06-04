import pyautogui
import time

id = open('id.txt', 'r').read()
subject = open('subject.txt', 'r').read()
message = open('message.txt', 'r').read()

pyautogui.press('win')
pyautogui.typewrite('google')
time.sleep(1)
pyautogui.press('enter')

pyautogui.moveTo(397, 62)
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite('mail')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(71, 187)
time.sleep(0.5)
pyautogui.click()

pyautogui.moveTo(1557, 777)
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite(message)

time.sleep(0.5)
pyautogui.moveTo(1406, 517)
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite(subject)

time.sleep(0.5)
pyautogui.moveTo(1402, 473)
pyautogui.click()
pyautogui.typewrite(id)

time.sleep(0.5)

pyautogui.hotkey('ctrl', 'enter')