import threading
import time
import os
import sys
from pynput import mouse
from pynput import keyboard


# import mouse
# import keyboard

# mouse_events = []
# keyboard_events = []
#
# keyboard.wait(".")
#
# mouse.hook(mouse_events.append)
# keyboard.hook_key(keyboard_events.append)
# # keyboard.start_recording()
#
# keyboard.wait(".")
#
# mouse.unhook(mouse_events.append)
# keyboard.unhook(keyboard_events.append)
#
# # keyboard_events = keyboard.stop_recording()
#
# for key in keyboard_events:
#     temp = str(key)
#     temp = temp.replace("("," ")
#     temp = temp.replace(")", "")
#     res = temp.split(" ")
#     print(res)
#     # print("\n")
#
# for key in mouse_events:
#     temp = str(key)
#     if temp.find("MoveEvent") != -1:
#         continue
#     temp = temp.replace("("," ")
#     temp = temp.replace(")", "")
#     res = temp.split(" ")
#     print(res)
#     # print("\n")

# Keyboard threadings:

# k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
# k_thread.start()

# Mouse threadings:

# m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
# m_thread.start()

# waiting for both threadings to be completed

# k_thread.join()
# m_thread.join()

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
    # if not pressed:
    #     # Stop listener
    #     return False


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

    if key == keyboard.Key.f10:
        with open(file_path, 'a') as f:
            f.write('done')
            f.write('\n')
        # Stop listener
        return False
    if key == keyboard.Key.f9:
        with open(file_path, 'a') as f:
            f.write('start')
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

# kl = keyboard.Listener(target = on_press, arg =(key=None))

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as k_listener, \
        mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()
