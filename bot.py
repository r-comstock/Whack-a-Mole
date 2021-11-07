import numpy as np
import cv2
import mss
import pyautogui
import time
import keyboard
from time import sleep
pyautogui.PAUSE = 0

#read in the replay image in gray scale
replay = cv2.imread('Assets/replay.png', 0)
bomb = cv2.imread('Assets/bomb.png', 0)
fortypointmole = cv2.imread('Assets/fortypointmole.png', 0)
home = cv2.imread('Assets/home.png', 0)
playbutton = cv2.imread('Assets/playbutton.png', 0)
tenpointmole = cv2.imread('Assets/tenpointmole.png', 0)
thirtypointmole = cv2.imread('Assets/thirtypointmole.png', 0)
twentypointmole = cv2.imread('Assets/twentypointmole.png', 0)
asset_images =[fortypointmole, tenpointmole, thirtypointmole, twentypointmole]

#Area of the game screen that we want to capture
dimensions = {'top': 345, 'left': 279, 'width': 913, 'height': 597}

before = np.array(mss.mss().grab(dimensions))
cv2.imshow('before', before)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Press s to start playing.")
print("Press q to quit.")
keyboard.wait('s')

while True:
    img = np.array(mss.mss().grab(dimensions))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img.save('screenshots/screenshot' + str(time.time()) + '.png')

    #check for asset images on the img
    for image in asset_images:
        result = cv2.matchTemplate(img, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        print(max_val)
        if max_val > 0.6:
            pyautogui.click(max_loc[0] + dimensions['left'], max_loc[1] + dimensions['top'])
        
    if keyboard.is_pressed('q'):
        break
