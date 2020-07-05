import pyautogui
import keyboard
import time
from PIL import ImageGrab

Fish = 0


if keyboard.is_pressed('F10'):
    pyautogui.moveTo(1580, 660)
    pyautogui.click(button='left', clicks=1)
    Hook = 1
    while True:
        image = ImageGrab.grab()
        x = 1580
        x1 = x - 90
        x2 = x + 90
        if Hook == 1:
            for y in range(200, 850):  # To check whether a fish's on the hook
                for x in range(x1, x2):
                    color = image.getpixel((x, y))
                    if color == (68, 252, 234):
                        print("Fish on Hook!")
                        Fish = 1
                        Hook = 0
                        t0 = time.clock()
                        break
        t1 = time.clock()
        if Fish == 1:
            pyautogui.click(button='left', clicks=1)
        elif image.getpixel((1170, 1010)) == (0, 0, 0) and Fish == 1 and t1 - t0 < 0.06:
            pyautogui.click(button='left', clicks=2, interval=0.85)
            continue
        elif image.getpixel((1170, 1010)) != (95, 255, 93) and Fish == 1:
            pyautogui.click(button='left', clicks=1)
            print ("ok")
            Hook = 1
            Fish = 0

