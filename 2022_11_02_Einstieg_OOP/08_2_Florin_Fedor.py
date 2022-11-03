import pgzrun

WIDTH = 512
HEIGHT = 512
TITLE = "Super Strong Alien Game"



alien = Actor('alien')
alien.pos = 100, 100
alien2 = Actor('alien')
alien2.pos = 100, 200


def draw():
    screen.clear()
    screen.blit("sterne.png", (0, 0))
    alien.draw()
    alien2.draw()


pgzrun.go()
