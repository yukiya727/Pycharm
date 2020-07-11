class Location():
    def __init__(self, locationName):
        self.locationName = locationName


class Farm():
    def __init__(self, animalsList):
        self.__animalsList = animalsList
        self.guardianDogs = [Dog("guardian", True) for count in range(2)]

    def getAnimalsList(self):
        return self.__animalsList

    def __erase(self):
        print("erasing all animals")
        self.__animalsList = []

    def __includeDogs(self):
        print("including guardian dogs")
        self.__animalsList += self.guardianDogs
        self.guardianDogs = []

    def __str__(self):
        returnString = "\nAnimals in the farm:\n"
        for animal in self.__animalsList:
            returnString += str(animal)
            returnString += "\n"
            returnString += "Guardian dogs:\n"
        for dog in self.guardianDogs:
            returnString += str(dog)
            returnString += "\n"
        return returnString

class Animal:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def __str__(self):
        return "%s is at the %s" % (self.name, self.location)

class Chicken(Animal):
    def __init__(self, name, location):
        super().__init__(name, location)

class Dog(Animal):
    def __init__(self, name, Angry = False, location = "Entrance"):
        super().__init__(name, location)

    def isAngry(self):
        return self.Angry()

def loadfarm(filename):
    try:
        f = open(filename,"r")
        f.readline()
        for line in f:
            name = str(line[0])
            location = str(line[1])
            Animal(name,location)
    except:
        print("Error: (File not found)")

loadfarm("Chicken_list.csv")

# f = Farm(chickenlist)
# print(f.__animalsList)
# print(f.getAnimalsList())
# print(f.guardianDogs)
# print(f)
# f._Farm__includeDogs()
# print(f)
# f._Farm__erase()
# print(f)
# f.__erase()