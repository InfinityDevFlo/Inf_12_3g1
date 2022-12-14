from item import Item

from abi2024 import DynArray
import utils


def LocationRequirement(interface):
    def check() -> bool:
        pass


class Location():

    def __init__(self, name: str, description: str, items: DynArray = DynArray(),
                 requirements: DynArray = DynArray(), **locs):
        self.name = name
        self.items = items
        self.description = description
        self.requirements = requirements
        self.north = locs.get("north", "Empty")
        self.east = locs.get("east", "Empty")
        self.south = locs.get("south", "Empty")
        self.west = locs.get("west", "Empty")

    def enter(self):
        print(self.description)
        utils.PLAYERINSTANCE.setLocation(self)

    def getNorth(self) -> str:
        return self.north

    def getEast(self) -> str:
        return self.east

    def getSouth(self) -> str:
        return self.south

    def getWest(self) -> str:
        return self.west

    def getDescription(self) -> str:
        return self.description

    def getItems(self) -> DynArray:
        return self.items

    def addItem(self, item: Item) -> "Location":
        self.items.append(item)
        return self

    def removeItem(self, item: Item) -> "Location":
        self.items.remove(item)
        return self

    def getRequirements(self) -> DynArray:
        return self.requirements

    def addRequirement(self, requirement: LocationRequirement) -> "Location":
        self.requirements.append(requirement)
        return self

    def removeRequirement(self, requirement: LocationRequirement) -> "Location":
        self.requirements.remove(requirement)
        return self

    def checkRequirements(self) -> bool:
        for requirement in self.requirements:
            if not requirement.check():
                return False
        return True


class Aula(Location):

    def __init__(self):
        super().__init__("Aula",
                         "Du befindest dich nun in der Aula. Vor dir siehst du die Bühne, während du in den Reihen stehst. Westlich von dir befindet sich das Foyer.",
                         west="Foyer", north="Bühne")


class Stage(Location):

    def __init__(self):
        super().__init__("Bühne", "", south="Aula")


class Foyer(Location):
    def __init__(self):
        super().__init__("Foyer", "", west="Aula")


class Sauelenhalle(Location):
    def __init__(self):
        super().__init__("Sauelenhalle", "", west="Foyer", north="Lehrerzimmer", east="Physik")


class Physik(Location):
    def __init__(self):
        super().__init__("Physik", "", north="Sauelenhalle", east="Chemie", west="Physikraum")


class Chemie(Location):
    def __init__(self):
        super().__init__("Chemie", "")


class Physikraum(Location):
    def __init__(self):
        super().__init__("Physikraum", "")


class Lehrerzimmer(Location):
    def __init__(self):
        super().__init__("Lehrerzimmer", "", south="Sauelehnalle")


class EmptyLocation(Location):

    def __init__(self):
        super().__init__("Nichts", "Hier ist nichts", north=None, east=None, south=None, west=None)


LOCATIONS = utils.Map()
LOCATIONS.put("Aula", Aula())
LOCATIONS.put("Bühne", Stage())
LOCATIONS.put("Foyer", Foyer())
LOCATIONS.put("Sauelenhalle", Sauelenhalle())
LOCATIONS.put("Physik", Physik())
LOCATIONS.put("Chemie", Chemie())
LOCATIONS.put("Physikraum", Physikraum())
LOCATIONS.put("Lehrerzimmer", Lehrerzimmer())
LOCATIONS.put("Empty", EmptyLocation())
