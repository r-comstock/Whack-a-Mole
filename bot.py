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
dimensions = {'top': 450, 'left': 550, 'width': 465, 'height': 420}

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
        if max_val > 0.9:
            pyautogui.click(max_loc[0] + dimensions['left'], max_loc[1] + dimensions['top'])
            #time.sleep(0.5)
        
    if keyboard.is_pressed('q'):
        break
"""
fps_time = time()

with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 0
    mon = sct.monitors[monitor_number]

    # Part of the screen to capture
    monitor = {
        "top": mon["top"] + 450,  # 100px from the top
        "left": mon["left"] + 550,  # 100px from the left
        "width": 465,
        "height": 420,
        "mon": monitor_number,
    }


while True:
    img = sct.grab(monitor)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    
    result = cv2.matchTemplate(img, replay, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.9:
        print("Replay button found.")
        #pyautogui.click(max_loc[0] + dimensions['left'], max_loc[1] + dimensions['top'])
        
    
    sleep(0.10)
    if keyboard.is_pressed('q'):
        break """

""" bomb = cv2.imread('Assets/bomb.png', 0)
replay = cv2.imread('Assets/replay.png', 0)

h, w = replay.shape

with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # Part of the screen to capture
    monitor = {
        "top": mon["top"] + 450,  # 100px from the top
        "left": mon["left"] + 550,  # 100px from the left
        "width": 465,
        "height": 420,
        "mon": monitor_number,
    }

    
img = sct.grab(monitor)
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)



result = cv2.matchTemplate(img, replay, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
location = max_loc
pyautogui.click((location[0] + w/2, location[1] + h/2))

cv2.rectangle(img, location, (location[0] + w, location[1] + h), (0, 0, 255), 2)
# Display the picture
cv2.imshow("OpenCV/Numpy normal", img)

cv2.waitKey(0)
cv2.destroyAllWindows()   """   