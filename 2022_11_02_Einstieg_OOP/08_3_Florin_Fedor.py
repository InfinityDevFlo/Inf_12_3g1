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

def update():
    
    if keyboard.left and alien.x > 1:
        alien.image = "alien-left"
        alien.x -= 1
    elif keyboard.right and alien.x < WIDTH:
        alien.image = "alien"
        alien.x += 1
    elif keyboard.up and alien.y > 1:
        alien.y -= 1
    elif keyboard.down and alien.y < HEIGHT:
        alien.y += 1
    elif keyboard.a and alien2.x > 1:
        alien2.image = "alien-left"
        alien2.x -= 1
    elif keyboard.d and alien2.x < WIDTH:
        alien2.image = "alien"
        alien2.x += 1
    elif keyboard.w and alien2.y > 1:
        alien2.y -= 1
    elif keyboard.s and alien2.y < HEIGHT:
        alien2.y += 1




pgzrun.go()
