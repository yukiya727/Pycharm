import threading
import time
import os
import sys
import keyboard
import pynput.mouse
import pynput.keyboard


def on_move(x, y):
    global file_path
    print('MouseMove,{0},{1},{2}'.format(
        x, y, time.time()))
    with open(file_path, 'a') as f:
        f.write('MouseMove,{0},{1},{2}'.format(x, y, time.time()))
        f.write('\n')


def on_click(x, y, button, pressed):
    global file_path
    print('{0},{1},{2},{3},{4}'.format(
        'MousePressed' if pressed else 'MouseReleased', button, x, y, time.time()))
    with open(file_path, 'a') as f:
        f.write('{0},{1},{2},{3},{4}'.format(
            'MousePressed' if pressed else 'MouseReleased', button, x, y, time.time()))
        f.write('\n')


def on_scroll(x, y, dx, dy):
    global file_path
    print('MouseScrolled,{0},{1},{2}'.format(
        x, y, time.time()))
    with open(file_path, 'a') as f:
        f.write('MouseScrolled,{0},{1},{2}'.format(
            x, y, time.time()))
        f.write('\n')


def on_press(key):
    global file_path
    try:
        print('KeyPressed,{0},{1}'.format(
            key.char, time.time()))
        with open(file_path, 'a') as f:
            f.write('KeyPressed,{0},{1}'.format(
                key.char, time.time()))
            f.write('\n')
    except AttributeError:
        print('KeyPressed,{0},{1}'.format(
            key, time.time()))
        with open(file_path, 'a') as f:
            f.write('KeyPressed,{0},{1}'.format(
                key, time.time()))
            f.write('\n')


def on_release(key):
    global file_path

    print('KeyReleased,{0},{1}'.format(
        key, time.time()))
    with open(file_path, 'a') as f:
        f.write('KeyReleased,{0},{1}'.format(
            key, time.time()))
        f.write('\n')

    if key == pynput.keyboard.Key.f10:
        with open(file_path, 'a') as f:
            f.write('done,{0}'.format(time.time()))
            f.write('\n')
        # Stop listener
        print(time.time()-t)
        pynput.mouse.Listener.stop(m_listener)
        return False
    if key == pynput.keyboard.Key.f8:
        with open(file_path, 'a') as f:
            f.write('start,{0}'.format(time.time()))
            f.write('\n')


# keyboard.wait(".")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = "pynput_record"
except:
    print('you must enter a name for the session\nfor example: python record.py session_name')
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_name = 'history.txt'
file_path = os.path.join(dir_path, file_name)
print(dir_path)

print("Please press 'F8' key to start recording")
keyboard.wait("F8")
t = time.time()

with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as k_listener, \
        pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()
