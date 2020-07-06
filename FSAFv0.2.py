import pyautogui
import pydirectinput
import keyboard
import time
from PIL import ImageGrab

hook, fish = (0, 0)


def throw_hook():
    global fish
    # pyautogui.dragTo(1580, 660, duration=0.1)
    pyautogui.click(button='left', clicks=1)
    fish = 0
    time.sleep(1)


def wait_for_fish():
    global fish, x, x1, x2, image
    for y in range(200, 850):
        for x in range(x1, x2):
            color = image.getpixel((x, y))
            if color == (68, 252, 234):
                # print("Fish on Hook!")
                pyautogui.click(button='left', clicks=1)
                image = ImageGrab.grab()
                fish = 1
                break
        if fish == 1:
            break


def capture_zone():
    global x, x1, x2, image
    image = ImageGrab.grab()
    x, y = pyautogui.position()
    x1 = x - 90
    x2 = x + 90


def catching_fish():
    global image, attempt
    for i in range(1080, 1380, 50):
        if image.getpixel((i, 1010)) == (0, 0, 0):
            pyautogui.click(button='left', clicks=1)
            attempt = True

stop = False

def main(stop):
    attempt = False
    while True:
        time.sleep(0.3)
        throw_hook()
        while True:
            if keyboard.is_pressed('F10'):
                terminate = True
            capture_zone()
            if fish == 0:
                wait_for_fish()
            if fish == 1:
                catching_fish()
                if image.getpixel((1585, 1015)) != (253, 112, 88) and attempt:
                    time.sleep(0.5)
                    throw_hook()
                    fish = 0
                    continue
        if stop:
            break