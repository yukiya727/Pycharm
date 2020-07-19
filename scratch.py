import autoit
import keyboard

# keyboard.wait(".")
# for i in range(15):
#      autoit.mouse_wheel("down", 1)

# autoit.mouse_click_drag(950, 470, 950, 475, button="right", speed=100)
# autoit.mouse_click_drag(950, 475, 965, 475, button="right", speed=50)

while True:
     keyboard.wait(".")
     print(autoit.mouse_get_pos())