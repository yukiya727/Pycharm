class Farm:
    def __init__(self, animals):
        self.animalList = animals

    def _erase(self):
        self.animalList = []

    def _addDogs(self):
        self.animalList += [Dog("AA-1", False) for i in range(2)]

    def getList(self):
        return self.animalList

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

D1 = [Dog("Bobby", True)]
print(D1[0])

F = Farm(D1)
print(F.getList())