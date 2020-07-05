import threading
import mouse
import keyboard

mouse_events = []
keyboard_events = []

keyboard.wait(".")

mouse.hook(mouse_events.append)
keyboard.start_recording()

keyboard.wait(".")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()

for key in keyboard_events:
    temp = str(key)
    temp = temp.replace("("," ")
    temp = temp.replace(")", "")
    res = temp.split(" ")
    print(res)
    # print("\n")

for key in mouse_events:
    temp = str(key)
    if temp.find("MoveEvent") != -1:
        continue
    temp = temp.replace("("," ")
    temp = temp.replace(")", "")
    res = temp.split(" ")
    print(res)
    # print("\n")

#Keyboard threadings:

# k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
# k_thread.start()

#Mouse threadings:

# m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
# m_thread.start()

#waiting for both threadings to be completed

# k_thread.join()
# m_thread.join()