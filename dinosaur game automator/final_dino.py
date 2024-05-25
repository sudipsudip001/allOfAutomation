import keyboard
import mss.tools
import cv2
import numpy
import pyautogui

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Press 'q' to quit.")
keyboard.wait('s')

sct = mss.mss()

x = 125
y = 380

dimensions = {
    'left': x,
    'top': y,
    'width': 75,
    'height': 95,
}

cactus1 = cv2.imread('cactus1.png')
cactus2 = cv2.imread('cactus2.png')
cactus3 = cv2.imread('cactus3.png')
cactus4 = cv2.imread('cactus4.png')
bird = cv2.imread('bird.png')

pictures = {
    'cactus1' : cactus1,
    'cactus2' : cactus2,
    'cactus3' : cactus3,
    'bird' : bird,
}

while True:
    scr = numpy.array(sct.grab(dimensions))[:, :, :3]

    for name, picture in pictures.items():
        result = cv2.matchTemplate(scr, picture, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.5:
            pyautogui.click(x=x, y=y)
            break

    cv2.imshow('Screen Shot', scr)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('q'):
        break

cv2.destroyAllWindows()