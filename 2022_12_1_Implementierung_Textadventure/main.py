from utils import *
import player
from location import *
from player import ACTIONS

running = True

if __name__ == "__main__":

    clearScreen()


    entry = """ 
          ______                 __     ___        __                        __        
         /_  __/  ___    _  __  / /_   /   |  ____/ / _   __  ___    ____   / /_  __  __   _____  ___ 
          / /    / _ \  | |/_/ / __/  / /| | / __  / | | / / / _ \  / __ \ / __/ / / / /  / ___/ / _ \\
         / /    /  __/ _>  <  / /_   / ___ |/ /_/ /  | |/ / /  __/ / / / // /_  / /_/ /  / /    /  __/
        /_/     \___/ /_/|_|  \__/  /_/  |_|\__,_/   |___/  \___/ /_/ /_/ \__/  \__,_/  /_/     \___/ 
                                                                                                
        \n\n
    """
    print(entry)

    print("Bitte wähle deinen Namen")
    name = input(">")

    player = player.Player(name)
    player.enterLocation("floor_2")

    utils.PLAYERINSTANCE = player

    while running:
        print("Was möchtest du tun?")
        print(f"Mögliche Aktionen: {arrayToSeparatedString(ACTIONS.keySet())}")
        action = input(">")

        if action == "quit":
            print("Auf Wiedersehen")
            running = False
            break

        if ACTIONS.containsKey(action):
            ACTIONS.get(action).execute(player)
        else:
            print("Das kannst du hier nicht tun")
