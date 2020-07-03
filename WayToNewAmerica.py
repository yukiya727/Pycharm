import time
import random

from values3 import *
from tools3 import *

file = open("AmericasMapA.csv")

x, y = (45, 53)
map = [[0 for i in range(y + 1)] for j in range(x + 1)]
x, y = (1, 1)

for line in file:
    items = line.strip().split(";")
    for i in range(len(items)):
        map[i + 1][y] = items[i]
    y += 1

ID = "1m1810477"
code = getSecretCode(ID, str(map[26][14]))

text_file = open("waypoint1.txt", "w")
text_file.write("Code: ")
text_file.write(code)
text_file.close()


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = getValue(x, y)

    def getValue(self):
        return self.value


class landTile(Tile):
    def __init__(self, x, y, priority):
        super().__init__(x, y)
        self.priority = priority

    def getPriority(self):
        return self.priority

    def __str__(self):
        if self.priority == "-":
            return "[ {0} , {1} ] is at priority of 0".format(x, y, self.priority)
        else:
            return "[ {0} , {1} ] is at priority of {2}]".format(x, y, self.priority)


p1 = map[26][14]
x, y = (26, 14)
text_file = open("waypoint2.txt", "w")
text = str(landTile(x, y, p1))
text_file.write(text)
text_file.close()

start = time.time()

goalx, goaly = (x, y)
count = 0
while True:
    if Tile(x, y).getValue() < Tile(goalx, goaly).getValue():
        x, y = (goalx, goaly)
        count += 1
        goalx += random.choice((-1, 0, 1))
        goaly += random.choice((-1, 0, 1))
        etime = time.time()
    if Tile(x, y).getValue() >= Tile(goalx, goaly).getValue():
        goalx += random.choice((-1, 0, 1))
        goaly += random.choice((-1, 0, 1))
    if count == 10:
        break

text_file = open("waypoint3.txt", "x")
text = "x: "
text_file.write(text)
text_file.write(x)
text_file.write('\n')
text = "y: "
text_file.write(text)
text_file.write(y)
text_file.write('\n')
text = "value: "
text_file.write(text)
text_file.write(getValue(x, y))
text_file.write('\n')
text = "priority: "
text_file.write(text)
text_file.write(map[x][y])
text_file.write('\n')
text = "elapsedTime: "
text_file.write(text)
text_file.write(etime)
text_file.write('\n')
text = "gold: "
text_file.write(text)
text_file.write(getGold(landTile(x, y).getValue(), etime))
text_file.write('\n')
text_file.close()

print()
end = time.time()
print(end - start)