from abi2024 import *
from item import Item
from location import Location
from location import LOCATIONS

class Player(object):
    inventorySize = 10

    def __init__(self, name: str, location: Location):
        self.name = name
        self.inventory = DynArray()
        self.location = location

        print(f"Willkommen {name}")

        print("Du kannst das Spiel jederzeit mit 'exit' oder 'quit' beenden.")

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

    def getLocation(self) -> Location:
        return self.location


    def getInventorySize(self) -> int:
        return self.inventorySize

    def enterLocation(self, locName: str) -> "Player":
        loc = LOCATIONS.get(locName)
        if loc.getRequirements().getLength() > 0:
            for requirement in loc.getRequirements():
                if not requirement.check():
                    print("Du kannst diesen Ort nicht betreten!")
                    return self
        self.location = loc
        print(self.location.getDescription())
        return self