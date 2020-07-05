import time
from values3 import *

v = ValuesMap()

def getSecretCode(studentID, priority):
    return "2"+str(studentID[0])+str(studentID[3])+str(priority)+str(studentID[-1])



def getValue(x, y):
    time.sleep(0.1)
    #return values[x*1000+y]
    return v._ValuesMap__values[x*1000+y]



def getGold(landTile, elapsedTime):
    return landTile.value*landTile.priority -24*elapsedTime



