import keyboard
import time
import pyautogui
import pydirectinput
import autoit
import pytesseract
import cv2
import mss
import numpy
from PIL import ImageGrab
import replay


def capture_image():
    global x, y
    global x1, x2, y1, y2
    global image
    image = ImageGrab.grab()
    x, y = autoit.mouse_get_pos()
    x1 = x - 90
    x2 = x + 90
    y1 = y - 300
    y2 = y + 300


def throw_hook(tx, ty):
    global fish
    autoit.mouse_move(tx, ty, 1)
    autoit.mouse_click('left')
    fish = False
    time.sleep(0.75)


def wait_for_fish():
    global fish, x, x1, x2, y1, y2, image
    for y in range(y1, y2):
        for x in range(x1, x2):
            color = image.getpixel((x, y))
            if color == (68, 252, 234):
                # print("Fish on Hook!") __legacy warning__
                autoit.mouse_click('left')
                image = ImageGrab.grab()
                fish = True
                break
        if fish:
            break


def catching_fish():
    global image, attempt
    for i in range(1080, 1380, 50):
        if image.getpixel((i, 1010)) == (0, 0, 0):
            autoit.mouse_click('left')
            attempt = True


def check_inventory():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    monitor = {"top": 1040, "left": 940, "width": 80, "height": 30}
    with mss.mss() as sct:
        # numpy.invert(sct.grab(monitor))
        img = cv2.cvtColor(numpy.array(numpy.invert(sct.grab(monitor))), cv2.COLOR_BGR2GRAY)
        # img = numpy.array(sct.grab(monitor))
    text = pytesseract.image_to_string(img)
    bag = text.split("/")
    print(text)
    # for item in bag:
    #     print(item)
    # if bag[0] == bag[2]:
    #     return True
    # else: return False


hook = False
fish = False
attempt = False
delay = 0.3
log, t_last = replay.load_replay()
r_spd = 1


def main(stop):
    global hook, fish, attempt, delay, log, t_last, r_spd

    while True:
        # First hook throwing
        x, y = (1580, 660)
        bagsize = 12 - 1

        time.sleep(delay)
        throw_hook(x, y)
        w_timer = time.time()
        while bagsize > 0:
            capture_image()
            if not fish:
                wait_for_fish()
                if time.time() - w_timer >= 10:
                    throw_hook(1580, 660)
            if fish:
                catching_fish()
                if image.getpixel((1585, 1015)) != (95, 255, 93) and attempt:
                    # # OCR function to check inventory, not workable with current version
                    # if check_inventory():
                    #     stop = True
                    #     break
                    time.sleep(delay)
                    throw_hook(1285, 400)  # *x y
                    fish = False
                    bagsize -= 1
                    w_timer = time.time()
                    continue
            if stop:
                break
        replay.play(log, r_spd, t_last)
        if stop:
            break
    print("Core program halted")
