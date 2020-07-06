# -*- coding: cp950 -*-
import time
import os
import sys
import keyboard
import pydirectinput
import autoit

pydirectinput.PAUSE = 0
pyautogui.PAUSE = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = "pynput_record"
except:
    print('you must enter a name for the session\nfor example: python replay.py session_name')
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)

file_name = 'history.txt'
file_path = os.path.join(dir_path, file_name)
# print(dir_path)

# open the recording file
with open(file_path, 'r') as f:
    steps = f.readlines()

# clean steps
new_steps = []
temp_step = []
t_last = 0.0
t_temp = 0.0
id = 0
startcount = False
pause = False

SpecialKeys = [
    "ctrl", "alt", "shift", "win"
]


def Keystring(str):
    global k, key_type

    def ifcontrolkey(dkey):
        global key_type
        if any(c in dkey for c in SpecialKeys):
            key_type = key_type.strip(" ")
        return dkey

    if k:
        k = False
        str = ifcontrolkey(str)
        return "{0}{1}{2}{3}".format("{", str, key_type, "}")
    if str.find("keypressed") != -1:
        k = True
        key_type = " down"
    if str.find("keyreleased") != -1:
        k = True
        key_type = " up"
    return str


lag_limit = 0.00
k_last = ""
skip = False

for step in steps:
    new_step = []
    k = False

    for i in step.split(','):
        # Reformat key string
        if i.find("Key.") != -1:
            i = i.replace("Key.", "")
        if i.find("Button.") != -1:
            i = i.replace("Button.", "")
        if i.find("'") != -1:
            i = i.replace("'", "")

        i = i.lower()
        i = Keystring(i)

        if i == k_last:
            print(k_last)
            skip = True
            break
        if i.find("{") != -1:
            k_last = i
        skip = False

        new_step.append(i.strip('\n'))

    if skip:
        continue

    if startcount != True:
        if new_step[0] != 'start':
            t_last = float(new_step[-1])
        if new_step[0] == 'start':
            startcount = True
            new_steps.append(new_step)
            continue
        continue

    if new_step[0] == 'mousemove' and id != 0:
        if new_steps[id - 1][0] == 'mousemove':
            if float(new_step[-1]) - t_last < lag_limit:
                temp_step = new_step
                t_temp = float(new_step[-1])
                pause = True
                continue
        t_last = float(new_step[-1])

    elif new_step[0] != 'mousemove' and id > 1:
        if new_steps[id - 1][0] == 'mousemove' and new_steps[id - 2][0] == 'mousemove' and pause == True:
            new_steps.append(temp_step)
            t_last = t_temp

    new_steps.append(new_step)
    pause = False
    id += 1

for step in new_steps:
    print(step)
print("Recorded objects:", len(new_steps))

t_last = float(new_steps[0][-1])
x = 1
tt = 0.0

print("Press '.' to replay")
keyboard.wait(".")

timer = time.time()

for step in new_steps:
    if step[0] == 'mousemove':
        time.sleep((float(step[-1]) - t_last) / x)
        autoit.mouse_move(int(step[1]), int(step[2]), 0)
        t_last = float(step[-1])
        continue

    if step[0] == 'mousepressed':
        time.sleep((float(step[-1]) - t_last) / x)
        autoit.mouse_move(int(step[2]), int(step[3]), 0)
        autoit.mouse_down(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'mousereleased':
        time.sleep((float(step[-1]) - t_last) / x)
        autoit.mouse_move(int(step[2]), int(step[3]), 0)
        autoit.mouse_up(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'keypressed':
        time.sleep((float(step[-1]) - t_last) / x)
        autoit.send(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'keyreleased':
        time.sleep((float(step[-1]) - t_last) / x)
        autoit.send(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'done':
        print('End autorun')
        print(time.time() - timer)
        sys.exit()
