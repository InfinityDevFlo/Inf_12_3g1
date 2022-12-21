from abi2024 import *
from item import Item
import utils
from location import Location
from location import LOCATIONS


class Player(object):
    inventorySize = 10

    def __init__(self, name: str):
        self.name = name
        self.inventory = DynArray()
        self.location = "floor_2"

        print(f"Willkommen {name}")

        print("Du kannst das Spiel jederzeit mit 'quit' beenden.")

        print("Bisschen Spielinformationen Dies Das")


    def getCurrentItemAmount(self) -> int:
        return self.inventory.getLength()

    def addItemToInventory(self, item: Item) -> "Player":
        self.inventory.append(item)
        return self

    def removeItemFromInventory(self, item: Item) -> "Player":
        self.inventory.remove(item)
        return self

    def getInventory(self) -> DynArray:
        return self.inventory


    def hasItem(self, item: Item) -> bool:
        for i in range(self.inventory.getLength()):
            if self.inventory.getItem(i).getId() == item.getId():
                return True
        return False

    def getLocation(self) -> Location:
        return LOCATIONS.get(self.location)


    def getInventorySize(self) -> int:
        return self.inventorySize

    def enterLocation(self, locName: str) -> "Player":
        loc = LOCATIONS.get(locName)
        if loc.getRequirements().getLength() > 0:
            for i in range(loc.getRequirements().getLength()):
                if not loc.getRequirements().getItem(i).check():
                    print("Du kannst diesen Raum nicht betreten.")
                    return self
        neighbors = LOCATIONS.get(self.location).getNeighborLocations()
        for i in range(neighbors.getLength()):
            locale = LOCATIONS.get(neighbors.getItem(i))
            ACTIONS.remove(locale.getName())
        self.location = loc.getId()
        for i in range(loc.getNeighborLocations().getLength()):
            locale = LOCATIONS.get(loc.getNeighborLocations().getItem(i))
            ACTIONS.put(locale.getName(), Move(locale.getId()))
        print(loc.getDescription())
        return self


class Action(object):

    def __init__(self, name: str):
        self.name = name

    def execute(self, player: Player):
        pass


class Loc(Action):

    def __init__(self):
        super().__init__("loc")

    def execute(self, player: Player):
        print(player.getLocation().getName())


class Move(Action):

    def __init__(self, loc: str):
        super().__init__("move")
        self.loc = loc

    def execute(self, player: Player):
        player.enterLocation(self.loc)


ACTIONS = utils.Map()
ACTIONS.put("loc", Loc())