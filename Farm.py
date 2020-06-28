class Animal():
    def __init__(self.name.initialLocation):
    self.name = name
    if isinstance(initialLocation,str):
        self.locationA =  initialLocation
    elif isinstance(initialLocation, Location):
        self.initialLocation.LocationName

class Dog(Animal):
    def __init__(self, name, angry = False):
        Animal.__init__(self, name, "Entrance")
        self.angry = angry

class Location():
    def __init__(self, locationName):
        self.locationName = locationName


class Farm():
    def __int__(self, animalslist):
        self.__animallist = animalslist
        self.guardianDogs = [Dog("guardian",True) for i in range(2)]

    def __str__(self):
        return "The farm has" + self.guardiandogs

    def __erase(self):
        self.animallist = []


d = Dog("Bobby")
print(d.name)