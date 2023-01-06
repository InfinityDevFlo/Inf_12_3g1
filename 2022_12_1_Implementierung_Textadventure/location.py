from item import Item

from abi2024 import DynArray
import utils
import item as ITEMS


class LocationRequirement(object):

    def __init__(self):
        pass

    def check(self) -> bool:
        pass


class Location(object):

    def __init__(self, id: str, name: str, description: str, locs: DynArray, items: DynArray = DynArray(),
                 requirements: DynArray = DynArray()):
        self.id = id
        self.name = name
        self.items = items
        self.description = description
        self.requirements = requirements
        self.neighbor_locs = locs

    def enter(self):
        print(self.description)
        utils.PLAYERINSTANCE.setLocation(self)

    def getNeighborLocations(self) -> DynArray:
        return self.neighbor_locs

    def getDescription(self) -> str:
        return self.description

    def getItems(self) -> DynArray:
        return self.items

    def addItem(self, item: Item) -> "Location":
        self.items.append(item)
        return self

    def removeItem(self, item: Item) -> "Location":
        index = None
        for i in range(self.items.getLength()):
            if self.items.getItem(i).getId() == item.getId():
                index = i
                break
        self.items.delete(index)
        return self

    def getRequirements(self) -> DynArray:
        return self.requirements

    def hasItem(self, id: str) -> bool:
        for i in range(self.items.getLength()):
            if self.items.getItem(i).getId() == id:
                return True
        return False

    def getItem(self, id: str) -> Item:
        for i in range(self.items.getLength()):
            if self.items.getItem(i).getId() == id:
                return self.items.getItem(i)
        return None

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

    def getName(self) -> str:
        return self.name

    def getItems(self) -> DynArray:
        return self.items

    def getId(self) -> str:
        return self.id


class Floor_1(Location):
    def __init__(self):
        neighbor_locs = DynArray()
        neighbor_locs.append("elevator")
        neighbor_locs.append("room_101")
        neighbor_locs.append("room_102")
        neighbor_locs.append("room_103")
        super().__init__("floor_1", "Flur 1", "Du befindest dich im Flur des ersten Stockwerkes", neighbor_locs)


class Floor_2(Location):

    def __init__(self):
        neighbor_locs = DynArray()
        neighbor_locs.append("elevator")
        neighbor_locs.append("room_201")
        neighbor_locs.append("room_202")
        neighbor_locs.append("room_203")

        super().__init__("floor_2", "Flur 2", "Du bist im Flur des 2. Stockwerkes", locs=neighbor_locs)


class Elevator(Location):

    def __init__(self):
        neighbor_locs = DynArray()
        neighbor_locs.append("exit")
        neighbor_locs.append("floor_1")
        neighbor_locs.append("floor_2")

        super().__init__("elevator", "Aufzug", "Du bist im Aufzug", locs=neighbor_locs)


class Room(Location):

    def __init__(self, number: int, floor: int, description: str, items: DynArray = DynArray(),
                 requirements: DynArray = DynArray()):
        self.number = number
        self.floor = floor
        neighbor_locs = DynArray()
        neighbor_locs.append("floor_" + str(floor))

        super().__init__(f"room_{floor}0{number}", f"Raum {floor}0{number}", description, neighbor_locs, items,
                         requirements)


class Raum_101(Room):

    def __init__(self):
        super().__init__(1, 1, "Du bist im Raum 101", DynArray(), DynArray())


class Raum_102(Room):

    def __init__(self):
        super().__init__(2, 1, "Du bist im Raum 102", DynArray(), DynArray())


class Raum_103(Room):

    def __init__(self):
        items = DynArray()
        items.append(ITEMS.Key())
        super().__init__(3, 1, "Du bist im Raum 103", items, DynArray())


class Raum_201(Room):

    def __init__(self):
        super().__init__(1, 2, "Du bist im Raum 201", DynArray(), DynArray())


class Raum_202(Room):

    def __init__(self):
        super().__init__(2, 2, "Du bist im Raum 202", DynArray(), DynArray())


class Room_203Requirement(LocationRequirement):

    def __init__(self):
        super().__init__()

    def check(self) -> bool:
        return input("Bitte Code eingeben: ") == "1984"


class Raum_203(Room):

    def __init__(self):
        items = DynArray()
        items.append(ITEMS.Key())
        requirements = DynArray()
        requirements.append(Room_203Requirement())
        super().__init__(3, 2, "Super! Du hast es geschafft den Code zu knacken. Auf dem Tisch im Zimmer siehst du einen Schlüssel. Den müssen die Reinigungskräfte hier wohl vergessen haben. ", items=items, requirements=requirements)


class ExitLocRequirement(LocationRequirement):

    def __init__(self):
        super().__init__()

    def check(self) -> bool:
        return utils.PLAYERINSTANCE.hasItem("key")


class Exit(Location):

    def __init__(self):
        requirements = DynArray()
        requirements.append(ExitLocRequirement())
        super().__init__("exit", "Exit", "Du bist im Ziel", DynArray(), DynArray(), requirements)


LOCATIONS = utils.Map()
LOCATIONS.put("floor_1", Floor_1())
LOCATIONS.put("floor_2", Floor_2())
LOCATIONS.put("elevator", Elevator())
LOCATIONS.put("room_101", Raum_101())
LOCATIONS.put("room_102", Raum_102())
LOCATIONS.put("room_103", Raum_103())
LOCATIONS.put("room_201", Raum_201())
LOCATIONS.put("room_202", Raum_202())
LOCATIONS.put("room_203", Raum_203())
LOCATIONS.put("exit", Exit())
