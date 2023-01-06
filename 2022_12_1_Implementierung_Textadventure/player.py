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

        print("""
Du bist im Flur des 2. Stockwerkes. eines Hotels. Dafür ist es hier aber doch erstaunlich ruhig.
Du merkst langsam, dass du hier alleine bist und möchtest raus. Du steigst in den Fahrstuhl und drückst auf "EG". Der Fahrstuhl fängt an sich zu bewegen und du fährst nach unten.
Unten angekommen stellst du fest, dass sich die Tür nicht öffnet. Auf dem kleinen Display im Fahrstuhl steht "Bitte Schlüssel einstecken um den Fahrstuhl zu öffnen". Du fährst wieder hoch in den zweiten Stock.
Schaffst du es den Schlüssel zu finden?""")


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


    def hasItem(self, id: str) -> bool:
        for i in range(self.inventory.getLength()):
            if self.inventory.getItem(i).getId() == id:
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
                    print("Du kannst diesen Raum noch nicht betreten. Du benötigst noch etwas.")
                    return self
        neighbors = LOCATIONS.get(self.location).getNeighborLocations()
        for i in range(neighbors.getLength()):
            locale = LOCATIONS.get(neighbors.getItem(i))
            ACTIONS.remove(f"gehe zu {locale.getName()}")
        for i in range(LOCATIONS.get(self.location).getItems().getLength()):
            item = LOCATIONS.get(self.location).getItems().getItem(i)
            ACTIONS.remove(f"{item.getName()} aufheben")
        if loc.getId() == "exit":
            print("Du hast das Spiel gewonnen!")
            quit()
        self.location = loc.getId()
        for i in range(loc.getNeighborLocations().getLength()):
            locale = LOCATIONS.get(loc.getNeighborLocations().getItem(i))
            ACTIONS.put(f"gehe zu(-m) {locale.getName()}", Move(locale.getId()))
        for i in range(loc.getItems().getLength()):
            item = loc.getItems().getItem(i)
            ACTIONS.put(f"{item.getName()} aufheben", Take(item.getId()))
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

class Take(Action):

    def __init__(self, item: str):
        super().__init__("take")
        self.item = item

    def execute(self, player: Player):
        if player.getCurrentItemAmount() < player.getInventorySize():
            if player.getLocation().hasItem(self.item):
                player.addItemToInventory(player.getLocation().getItem(self.item))
                player.getLocation().removeItem(player.getLocation().getItem(self.item))
                print(f"Du hast das Item {self.item} aufgenommen.")
            else:
                print("Dieses Item befindet sich nicht in diesem Raum.")
        else:
            print("Dein Inventar ist voll.")

ACTIONS = utils.Map()
# ACTIONS.put("loc", Loc()) # Debug command zum anzeigen der aktuellen Location


