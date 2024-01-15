import pgzrun

WIDTH = 500
HEIGHT = 500

#calls the image alien.png and sets the location on the screen
alien = Actor('alien')
alien.x = 0
alien.y = 50


#draws the screen
def draw():
    screen.clear()
    alien.draw()

#moves the alien to the right and down
def update():
    alien.x += 10
    if alien.x > WIDTH:
        alien.x = 0
        alien.y=alien.y+20
'''
#commented out, but would moves the alien based on keystrokes
def update():
    if keyboard.s:
        alien.x = alien.x + 2
    elif keyboard.a:
        alien.x = alien.x - 2
    elif keyboard.up:
        alien.y+=-2
    elif keyboard.down:
        alien.y+=2
'''
pgzrun.go()