# -*- coding: cp950 -*-
import time
import os
import sys
import keyboard
import pydirectinput
import pydirectinput

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

for step in steps:
    new_step = []
    for i in step.split(','):
        if step.find("Key.") != -1:
            step.replace("Key.", "")
        new_step.append(i.strip('\n'))

    if startcount != True:
        if new_step[0] != 'start' and new_step[0] != 'done':
            t_last = float(new_step[-1])
        if new_step[0] == 'start':
            startcount = True
        continue

    if new_step[0] == 'MouseMove' and id != 0:
        if new_steps[id-1][0] == 'MouseMove':
            if float(new_step[-1]) - t_last < 0.1:
                temp_step = new_step
                t_temp = float(new_step[-1])
                continue
        t_last = float(new_step[-1])

    elif new_step[0] != 'MouseMove' and id > 1:
        if new_steps[id - 1][0] == 'MouseMove' and new_steps[id - 2][0] == 'MouseMove':
            new_steps.append(temp_step)
            t_last = t_temp


    new_steps.append(new_step)
    id += 1

print("Recorded objects:", len(new_steps))

# start moving mouse cursor
t_last = float(new_steps[0][-1])

print("Press F9 to replay")
keyboard.wait("F9")

for step in new_steps:


    if step[0] == 'MousePressed' and step[1] == 'Button.left':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.moveTo(int(step[2]), int(step[3]))
        pydirectinput.mouseDown(button='left')
        t_last = float(step[-1])
        continue

    if step[0] == 'MouseReleased' and step[1] == 'Button.left':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.moveTo(int(step[2]), int(step[3]))
        pydirectinput.mouseUp(button='left')
        t_last = float(step[-1])
        continue

    if step[0] == 'MousePressed' and step[1] == 'Button.right':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.moveTo(int(step[2]), int(step[3]))
        pydirectinput.mouseDown(button='right')
        t_last = float(step[-1])
        continue

    if step[0] == 'MouseReleased' and step[1] == 'Button.right':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.moveTo(int(step[2]), int(step[3]))
        pydirectinput.mouseUp(button='right')
        t_last = float(step[-1])
        continue

    if step[0] == 'KeyPressed':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.keyDown(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'KeyReleased':
        time.sleep(float(step[-1]) - t_last)
        pydirectinput.keyUp(step[1])
        t_last = float(step[-1])
        continue

    if step[0] == 'done':
        print('End autorun')
        sys.exit()
