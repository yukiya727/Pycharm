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


f = Farm(chickenlist)
# print(f.__animalsList)
print(f.getAnimalsList())
print(f.guardianDogs)
print(f)
f._Farm__includeDogs()
print(f)
f._Farm__erase()
print(f)
f.__erase()
