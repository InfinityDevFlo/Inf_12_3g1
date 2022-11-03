import pgzrun

WIDTH = 512 # Breite des Fensters
HEIGHT = 512 # Höhe des Fensters
TITLE = "Game title" # Titel des Fensters


def draw():
    screen.clear() # Bildschirminhalt löschne
    screen.fill((255, 255, 0)) # Bildschirm mit gelb füllen
    screen.blit("sterne.png", (0, 0)) # Bild als Hintergrund setzen
    # Wenn erst blit und dann fill, wird das Bild mit gelb überschrieben


pgzrun.go()
