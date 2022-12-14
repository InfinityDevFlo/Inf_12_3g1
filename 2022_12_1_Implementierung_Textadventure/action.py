from player import Player
from location import Location
import utils



class Action(object):

    def __init__(self, name: str):
        self.name = name


    def execute(self, player: Player):
        pass

class North(Action):

    def __init__(self):
        super().__init__("north")

    def execute(self, player: Player):
        location = player.getLocation().getNorth()
        player.enterLocation(location)


class South(Action):

    def __init__(self):
        super().__init__("south")

    def execute(self, player: Player):
        location = player.getLocation().getSouth()
        player.enterLocation(location)


class East(Action):

    def __init__(self):
        super().__init__("east")

    def execute(self, player: Player):
        location = player.getLocation().getEast()
        player.enterLocation(location)

class West(Action):

    def __init__(self):
        super().__init__("west")

    def execute(self, player: Player):
        location = player.getLocation().getWest()
        player.enterLocation(location)

class Loc(Action):

    def __init__(self):
        super().__init__("loc")

    def execute(self, player: Player):
        print(player.getLocation().name)

ACTIONS = utils.Map()
ACTIONS.put("north", North())
ACTIONS.put("south", South())
ACTIONS.put("east", East())
ACTIONS.put("west", West())
ACTIONS.put("loc", Loc())