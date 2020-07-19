import autoit
import keyboard

# keyboard.wait(".")
# for i in range(15):
#      autoit.mouse_wheel("down", 1)

# autoit.mouse_click_drag(950, 470, 950, 475, button="right", speed=100)
# autoit.mouse_click_drag(950, 475, 965, 475, button="right", speed=50)

# while True:
#      keyboard.wait(".")
#      print(autoit.mouse_get_pos())
a = 60
b = 75
L = a + b 
ai = a / L
bi = 1 - ai
q = 35
c = 36.75 / q + 0.1 + 0.03 * q
n = (bi * L) / 15
nn = 35
beta = (ai * 15) / (bi * (nn - 15))
qu = (bi * L) / n
qc = L * (ai + (bi*beta)) / (n * beta)
print(qu)
print(qc)
