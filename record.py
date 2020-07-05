import time
import os
import sys
from functools import partial
import keyboard
import pyHook
import pythoncom
import pyautogui


def left_down(event, file_path):
    x, y = event.Position
    print(",".join(['left_down', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['left_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def left_up(event, file_path):
    x, y = event.Position
    print(",".join(['left_up', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['left_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def right_down(event, file_path):
    x, y = event.Position
    print(",".join(['right_down', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['right_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def right_up(event, file_path):
    x, y = event.Position
    print(",".join(['right_up', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['right_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def key_down(event, file_path):
    if event.KeyID == 110:
        print("End of recording")
        with open(file_path, 'a') as f:
            f.write('done')
        sys.exit()
    id = str(event.KeyID)
    print(",".join(['key_down', id]))
    with open(file_path, 'a') as f:
        f.write(",".join(['key_down', id]))
        f.write('\n')
    return True


def key_up(event, file_path):
    id = str(event.KeyID)
    print(",".join(['key_up', id]))
    with open(file_path, 'a') as f:
        f.write(",".join(['key_up', id]))
        f.write('\n')
    return True


def OnKeyboardEvent(event, file_path, dir_path):
    id = str(event.KeyID)
    print(",".join(['key_down', id]))
    if event.KeyID == 110:
        print("End of recording")
        with open(file_path, 'a') as f:
            f.write('done')
        sys.exit()
    print(event.KeyID)
    return True


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    directory = 'mouse_recorder'
    try:
        session_name = "python_record"
    except:
        print('you must enter a name for the session\nfor example: python record.py session_name')
        sys.exit()
    dir_path = os.path.join(os.getcwd(), directory, session_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = 'history.txt'
    file_path = os.path.join(dir_path, file_name)
    print(dir_path)

    keyboard.wait(".")
    print("Start recording")

    ld = partial(left_down, file_path=file_path)
    lu = partial(left_up, file_path=file_path)
    rd = partial(right_down, file_path=file_path)
    ru = partial(right_up, file_path=file_path)



    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(ld)
    hm.SubscribeMouseLeftUp(lu)
    hm.SubscribeMouseRightDown(rd)
    hm.SubscribeMouseRightUp(ru)
    hm.HookMouse()

    kd = partial(key_down, file_path=file_path)
    ku = partial(key_up, file_path=file_path)

    hm.KeyDown = kd
    hm.KeyUp = ku
    hm.HookKeyboard()

    # oke = partial(OnKeyboardEvent, file_path=file_path, dir_path=dir_path)
    #
    # hm.KeyDown = oke
    # hm.HookKeyboard()

    # while True:
    #    pythoncom.PumpWaitingMessages()
    pythoncom.PumpMessages()

    hm.UnhookMouse()
    hm.UnHookKeyboard()
